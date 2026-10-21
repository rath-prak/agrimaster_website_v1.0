(function(){var last=null;setInterval(function(){fetch('/__version?'+Date.now()).then(r=>r.text()).then(v=>{if(last&&v!==last)location.reload();last=v;}).catch(()=>{});},1000);})();
