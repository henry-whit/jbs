let dc;
async function getData(){
    try{
        const r = await fetch('/getall')
        if(!r.ok){
            return;
        }
        docs = await r.json();
        const st = document.getElementById('st');
        for(const doc of docs){
            if(doc.completed === false){
                const item = document.createElement('div');
                const h = document.createElement('h2');
                h.textContent = doc["email"];
                const p = document.createElement('p');
                p.textContent = doc["description"];
                const form = document.createElement('form');
                form.action = `/complete?key=${doc['id']}`;
                const s = document.createElement('strong');
                const lb = document.createElement('label');
                lb.setAttribute("for","res");
                lb.textContent = "Upload result";
                const ip = document.createElement('input');
                ip.type = "file";
                ip.id = "res";
                const bt = document.createElement('button');
                bt.type = "submit";
                bt.textContent = "Complete";
                const hidden = document.createElement('input');
                hidden.type = "hidden";
                hidden.name = "key";
                hidden.value = doc["id"];
                form.appendChild(hidden);
                s.appendChild(lb);
                form.appendChild(s);
                form.appendChild(ip);
                form.appendChild(bt);
                item.appendChild(h);
                item.appendChild(p);
                item.appendChild(form);
                st.append(item);
            }
        }
    } catch(error){}
}
window.onload = getData;
