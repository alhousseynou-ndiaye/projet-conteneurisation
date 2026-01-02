async function loadETL() {
  const r = await fetch(`/api/etl/load`, { method: "POST" });
  const j = await r.json();
  document.getElementById("status").textContent = JSON.stringify(j, null, 2);
}

async function refresh() {
  const r = await fetch(`/api/data?limit=20`);
  const j = await r.json();
  document.getElementById("data").textContent = JSON.stringify(j, null, 2);
}

document.getElementById("load").onclick = loadETL;
document.getElementById("refresh").onclick = refresh;

refresh();
