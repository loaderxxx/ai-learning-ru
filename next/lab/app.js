'use strict';
const $ = id => document.getElementById(id);
let meta = null, last = null, revision = 0, busy = false;
function invalidate() {
  revision++; last = null; $('review').checked = false; $('download').disabled = true;
  $('review-box').hidden = true; $('result').replaceChildren();
  $('status').className = ''; $('status').textContent = 'Исходник или режим изменён. Запустите разбор заново.';
}
function message(text, error=false) { $('status').textContent = text; $('status').className = error ? 'error' : ''; }
async function getJSON(url, options) {
  const response = await fetch(url, options); const data = await response.json();
  if (!response.ok) throw new Error(data.error || 'Не удалось выполнить запрос.'); return data;
}
function render(data) {
  $('result').replaceChildren();
  for (const [key, label] of Object.entries(meta.labels)) {
    const item = data.card[key], block = document.createElement('article'); block.className='fact';
    const title = document.createElement('h3'); title.textContent=label;
    const value = document.createElement('div'); value.className='value' + (item.value === null ? ' unknown' : '');
    value.textContent = item.value === null ? 'Нет данных' : item.value; block.append(title,value);
    if (item.quote !== null) { const quote=document.createElement('p');quote.className='quote';quote.textContent='Источник: «'+item.quote+'»';block.append(quote); }
    $('result').append(block);
  }
  $('review-box').hidden=false;
}
$('note').addEventListener('input', invalidate);
$('mode').addEventListener('change', () => {invalidate();$('mode-note').textContent=$('mode').value==='demo'?'Деморежим показывает готовый разбор учебного примера без вызова модели.':'Сначала выберите локальную модель и отключите облачные функции в настройках Ollama по уроку.';});
$('example').addEventListener('click', async () => {try {const d=await getJSON('/api/example');$('note').value=d.text;invalidate();message('Пример загружен. Теперь соберите карточку.');} catch(e){message(e.message,true);}});
$('form').addEventListener('submit', async e => {
  e.preventDefault(); if(busy)return;
  invalidate();const ticket=revision;busy=true;$('run').disabled=true;$('example').disabled=true;
  message('Разбираем заметку… Не закрывайте страницу.');
  try {
    if (!meta) meta=await getJSON('/api/meta');
    const data=await getJSON('/api/extract',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text:$('note').value,mode:$('mode').value})});
    if(ticket!==revision){message('Текст изменился во время обработки. Старый ответ отброшен; запустите новый разбор.');return;}
    last=data;render(data);message((data.mode==='demo'?'Готов учебный разбор без модели.':'Ответ модели получен.')+' Проверьте значения и цитаты.');
  }catch(err){if(ticket===revision)message(err.message,true);}finally{busy=false;$('run').disabled=false;$('example').disabled=false;}
});
$('review').addEventListener('change',() => {$('download').disabled=!last||!$('review').checked;});
$('download').addEventListener('click',() => {
  if(!last||!$('review').checked)return;
  const payload={...last,human_reviewed:true,review_kind:'self_attestation',reviewed_at:new Date().toISOString()};
  const blob=new Blob([JSON.stringify(payload,null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);
  const a=document.createElement('a');a.href=url;a.download='checked-note.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
});
getJSON('/api/meta').then(d=>{meta=d;$('backend').textContent=d.model?'Модель сервера: '+d.model:'Модель не настроена. Учебный пример работает сразу.';}).catch(e=>message(e.message,true));
