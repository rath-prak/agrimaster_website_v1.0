const c=new URLSearchParams(location.search).get("topic"),t=document.getElementById("topic");c&&t&&[...t.options].forEach(e=>{e.text===c&&(t.value=e.text)});
