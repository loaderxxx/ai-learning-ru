// Node 18+. Tests actual app.js with a minimal DOM double, NOT a browser renderer.
// Start the Python server on 127.0.0.1:8765 before running this file.
const fs=require('node:fs'), path=require('node:path'), vm=require('node:vm'), assert=require('node:assert/strict');
const base='http://127.0.0.1:8765';
class Element {
  constructor(tag){this.tag=tag;this.listeners={};this.children=[];this.value='';this.checked=false;this.disabled=false;this.hidden=false;this.textContent='';}
  addEventListener(name,fn){this.listeners[name]=fn;}
  append(...items){this.children.push(...items);}
  replaceChildren(...items){this.children=[...items];}
  click(){return this.listeners.click?.({preventDefault(){}});}
  fire(name){return this.listeners[name]?.({preventDefault(){}});}
}
(async()=>{
 const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
 const elements=Object.fromEntries([...html.matchAll(/id="([^"]+)"/g)].map(m=>[m[1],new Element(m[1])]));
 elements.mode.value='demo';let downloaded=null;let delay=null;
 const document={getElementById:id=>{assert.ok(elements[id],id);return elements[id];},createElement:tag=>new Element(tag)};
 const wrappedFetch=async(url,opts={})=>{
   const response=await fetch(base+url,{...opts,headers:{...opts.headers,Origin:base}});
   if(url==='/api/extract'&&delay)await delay;
   return response;
 };
 const sandbox={document,fetch:wrappedFetch,Blob,URL:{createObjectURL:b=>{downloaded=b;return 'blob:test';},revokeObjectURL(){}},setTimeout,console};
 vm.createContext(sandbox);vm.runInContext(fs.readFileSync(path.join(__dirname,'app.js'),'utf8'),sandbox);
 await elements.example.click();await elements.form.fire('submit');
 assert.equal(elements.result.children.length,6,elements.status.textContent);
 assert.equal(elements.result.children.filter(x=>x.children[1].textContent==='Нет данных').length,3);
 assert.equal(elements.download.disabled,true);
 elements.review.checked=true;await elements.review.fire('change');await elements.download.click();
 const exported=JSON.parse(await downloaded.text());assert.equal(exported.human_reviewed,true);assert.equal(exported.card.price_rub.value,'1500');
 elements.note.value='Изменённая заметка';await elements.note.fire('input');
 assert.equal(elements.download.disabled,true);assert.equal(elements['review-box'].hidden,true);
 await elements.form.fire('submit');assert.match(elements.status.textContent,/Деморежим знает только/);
 await elements.example.click();let release;delay=new Promise(r=>{release=r;});
 const pending=elements.form.fire('submit');
 elements.note.value='Редакция во время обработки';await elements.note.fire('input');release();await pending;delay=null;
 assert.equal(elements.result.children.length,0);assert.match(elements.status.textContent,/Старый ответ отброшен/);
 elements.mode.value='ollama';await elements.mode.fire('change');await elements.form.fire('submit');
 assert.match(elements.status.textContent,/Укажите имя установленной модели/);
 console.log(JSON.stringify({kind:'JavaScript state checks with DOM double and real local HTTP',checks:6,result:'passed',browser_rendering:false,external_model_calls:0}));
})().catch(e=>{console.error(e);process.exitCode=1;});
