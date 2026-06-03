/* ------------------------------------------------------------------
 *  Mockup of the Compose UI.
 * ------------------------------------------------------------------ */
const state = {
  tab: "calendar",
  visibleMonth: new Date(new Date().getFullYear(), new Date().getMonth(), 1),
  selectedDate: todayISO(0),
  history: [] // stack of overlay screens like assignment-edit / truck-edit etc
};

const screenEls = {};
document.querySelectorAll('.screen').forEach(el => screenEls[el.dataset.screenId] = el);

function fmtJPDate(iso) {
  const d = new Date(iso);
  const w = ["日","月","火","水","木","金","土"][d.getDay()];
  return `${d.getFullYear()}年${d.getMonth()+1}月${d.getDate()}日(${w})`;
}
function ym(d) { return `${d.getFullYear()}年${d.getMonth()+1}月`; }

function showScreen(id) {
  Object.values(screenEls).forEach(el => el.hidden = true);
  screenEls[id].hidden = false;
}

function setTab(name) {
  state.tab = name;
  state.history = [];
  document.querySelectorAll('.nav-item').forEach(b => b.classList.toggle('active', b.dataset.nav === name));
  renderTab();
}

function pushOverlay(id, rendererFn) {
  state.history.push({ id, rendererFn });
  rendererFn();
  showScreen(id);
}
function popOverlay() {
  state.history.pop();
  if (state.history.length === 0) {
    renderTab();
  } else {
    const top = state.history[state.history.length-1];
    top.rendererFn();
    showScreen(top.id);
  }
}

function renderTab() {
  switch (state.tab) {
    case "calendar": renderCalendar(); showScreen("calendar"); break;
    case "trucks":   renderTrucks();   showScreen("trucks"); break;
    case "drivers":  renderDrivers();  showScreen("drivers"); break;
    case "clients":  renderClients();  showScreen("clients"); break;
  }
}

/* ---------- Calendar Screen ---------- */
function renderCalendar() {
  const el = screenEls.calendar;
  const visibleMonth = state.visibleMonth;
  const datesWithAssignments = new Set(assignments.map(a => a.date));
  const todayStr = todayISO(0);

  const daysOf = [];
  const first = new Date(visibleMonth.getFullYear(), visibleMonth.getMonth(), 1);
  const leading = first.getDay(); // Sun=0
  const dim = new Date(visibleMonth.getFullYear(), visibleMonth.getMonth()+1, 0).getDate();
  for (let i = 0; i < leading; i++) daysOf.push(null);
  for (let d = 1; d <= dim; d++) {
    const date = new Date(visibleMonth.getFullYear(), visibleMonth.getMonth(), d);
    daysOf.push(date);
  }
  while (daysOf.length % 7 !== 0) daysOf.push(null);

  const isoOf = d => `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  const dayCells = daysOf.map(date => {
    if (!date) return `<div class="day empty"></div>`;
    const iso = isoOf(date);
    const klass = [
      "day",
      date.getDay() === 0 ? "sun" : "",
      date.getDay() === 6 ? "sat" : "",
      iso === todayStr ? "today" : "",
      iso === state.selectedDate ? "selected" : ""
    ].filter(Boolean).join(" ");
    const dot = datesWithAssignments.has(iso) ? `<div class="dot"></div>` : "";
    return `<div class="${klass}" data-date="${iso}">${date.getDate()}${dot}</div>`;
  }).join("");

  const todays = assignments
    .filter(a => a.date === state.selectedDate)
    .sort((a,b) => (a.departureTime||"").localeCompare(b.departureTime||""));

  const cards = todays.length === 0
    ? `<div class="empty-state">この日の配車はまだありません</div>`
    : todays.map(a => {
        const t = findTruck(a.truckId);
        const d = findDriver(a.driverId);
        const g = findClient(a.generatorClientId);
        const dis = findClient(a.disposalClientId);
        const statusClass = a.containerStatus.toLowerCase();
        return `
        <div class="card" data-assignment="${a.id}">
          <div class="row">
            <span class="time-pill">${a.departureTime||"--:--"} ▶ ${a.returnTime||"--:--"}</span>
            <span class="chip ${statusClass}">${ContainerStatus[a.containerStatus]}</span>
          </div>
          <div class="meta">
            <div><span class="label">車両:</span> ${t ? `${t.plateNumber} (${t.vehicleType})` : "車両未割当"}</div>
            <div><span class="label">ドライバー:</span> ${d ? d.name : "ドライバー未割当"}</div>
            <div><span class="label">排出元:</span> ${g ? g.name : "排出元未設定"}</div>
            <div><span class="label">行き先:</span> ${dis ? dis.name : "処分先未設定"}</div>
            ${a.wasteType ? `<div class="sub">廃棄物: ${a.wasteType}</div>` : ""}
            ${a.notes ? `<div class="sub">備考: ${a.notes}</div>` : ""}
          </div>
        </div>`;
      }).join("");

  el.innerHTML = `
    <div class="top-bar"><h2>配車カレンダー</h2></div>
    <div class="scroll-area">
      <div class="month-header">
        <button data-month="-1"><span class="material-symbols-outlined">chevron_left</span></button>
        <h3>${ym(visibleMonth)}</h3>
        <button data-month="1"><span class="material-symbols-outlined">chevron_right</span></button>
      </div>
      <div class="weekdays">
        <div class="sun">日</div><div>月</div><div>火</div><div>水</div><div>木</div><div>金</div><div class="sat">土</div>
      </div>
      <div class="days">${dayCells}</div>
      <div class="section-header">
        <div class="title">${fmtJPDate(state.selectedDate)}</div>
        <div class="count">${todays.length} 件</div>
      </div>
      <div class="list">${cards}</div>
    </div>
    <button class="fab" data-fab="add-assignment"><span class="material-symbols-outlined">add</span></button>
  `;

  // Wire up
  el.querySelectorAll('.day').forEach(c => c.addEventListener('click', () => {
    state.selectedDate = c.dataset.date;
    renderCalendar();
  }));
  el.querySelectorAll('button[data-month]').forEach(b => b.addEventListener('click', () => {
    const m = parseInt(b.dataset.month,10);
    state.visibleMonth = new Date(state.visibleMonth.getFullYear(), state.visibleMonth.getMonth()+m, 1);
    renderCalendar();
  }));
  el.querySelectorAll('[data-assignment]').forEach(card => card.addEventListener('click', () => {
    const id = parseInt(card.dataset.assignment,10);
    openAssignmentEdit(id);
  }));
  el.querySelector('[data-fab=add-assignment]').addEventListener('click', () => openAssignmentEdit(0));
}

/* ---------- Assignment Edit ---------- */
function openAssignmentEdit(id) {
  pushOverlay("assignment-edit", () => renderAssignmentEdit(id));
}
function renderAssignmentEdit(id) {
  const el = screenEls["assignment-edit"];
  const isNew = id === 0;
  const a = isNew
    ? { date: state.selectedDate, truckId: null, driverId: null, generatorClientId: null, disposalClientId: null,
        wasteType:"", departureTime:"", returnTime:"", containerStatus:"EMPTY", notes:"" }
    : assignments.find(x => x.id === id);

  const t = a.truckId   ? findTruck(a.truckId) : null;
  const d = a.driverId  ? findDriver(a.driverId) : null;
  const g = a.generatorClientId ? findClient(a.generatorClientId) : null;
  const dis = a.disposalClientId ? findClient(a.disposalClientId) : null;

  const chipFor = (key) => `<button class="filter-chip ${a.containerStatus===key?'selected':''}" data-status="${key}">${ContainerStatus[key]}</button>`;

  el.innerHTML = `
    <div class="top-bar">
      <button class="icon-btn" data-back><span class="material-symbols-outlined">arrow_back</span></button>
      <h2>${isNew ? "新規配車" : "配車編集"} — ${fmtJPDate(a.date)}</h2>
      ${isNew ? "" : `<button class="icon-btn" data-delete><span class="material-symbols-outlined">delete</span></button>`}
    </div>
    <div class="scroll-area">
      <div class="edit-form">
        <div class="field readonly"><label>車両</label>
          <div class="value">${t ? `${t.plateNumber} / ${t.vehicleType} (${BodyType[t.bodyType]})` : "—"}</div>
          <span class="trail material-symbols-outlined">expand_more</span>
        </div>
        <div class="field readonly"><label>ドライバー</label>
          <div class="value">${d ? `${d.name} (${d.licenseClass||"—"})` : "—"}</div>
          <span class="trail material-symbols-outlined">expand_more</span>
        </div>
        <div class="field readonly"><label>排出元 (取引先)</label>
          <div class="value">${g ? g.name : "—"}</div>
          <span class="trail material-symbols-outlined">expand_more</span>
        </div>
        <div class="field readonly"><label>行き先 (処分場/中間処理)</label>
          <div class="value">${dis ? dis.name : "—"}</div>
          <span class="trail material-symbols-outlined">expand_more</span>
        </div>
        <div class="field"><label>廃棄物種類</label>
          <div class="value">${a.wasteType || "&nbsp;"}</div>
        </div>
        <div class="row-2">
          <div class="field readonly"><label>発車予定</label>
            <div class="value">${a.departureTime || "--:--"}</div>
            <span class="trail material-symbols-outlined">schedule</span>
          </div>
          <div class="field readonly"><label>帰着予定</label>
            <div class="value">${a.returnTime || "--:--"}</div>
            <span class="trail material-symbols-outlined">schedule</span>
          </div>
        </div>
        <div>
          <div style="font-size:13px;font-weight:600;margin:4px 2px 8px;">車両の状態</div>
          <div class="chip-group">
            ${Object.keys(ContainerStatus).map(chipFor).join("")}
          </div>
        </div>
        <div class="field multiline"><label>備考</label>
          <div class="value">${a.notes || "&nbsp;"}</div>
        </div>
        <button class="btn-primary">${isNew ? "登録" : "更新"}</button>
      </div>
    </div>
  `;
  el.querySelector('[data-back]').addEventListener('click', popOverlay);
  el.querySelectorAll('[data-status]').forEach(b => b.addEventListener('click', () => {
    a.containerStatus = b.dataset.status;
    renderAssignmentEdit(id);
  }));
}

/* ---------- Trucks ---------- */
function renderTrucks() {
  const el = screenEls.trucks;
  const cards = trucks.map(t => `
    <div class="card" data-truck="${t.id}">
      <div class="master-title">${t.plateNumber}</div>
      <div class="master-meta">${t.vehicleType} / ${BodyType[t.bodyType]} / 積載 ${t.loadCapacityKg.toLocaleString()} kg</div>
      ${t.makerModel ? `<div class="master-meta">${t.makerModel}</div>` : ""}
    </div>
  `).join("");
  el.innerHTML = `
    <div class="top-bar"><h2>車両一覧</h2></div>
    <div class="scroll-area"><div class="list">${cards}</div></div>
    <button class="fab" data-fab="add-truck"><span class="material-symbols-outlined">add</span></button>
  `;
  el.querySelectorAll('[data-truck]').forEach(c => c.addEventListener('click', () => {
    openTruckEdit(parseInt(c.dataset.truck,10));
  }));
  el.querySelector('[data-fab=add-truck]').addEventListener('click', () => openTruckEdit(0));
}
function openTruckEdit(id) {
  pushOverlay("truck-edit", () => renderTruckEdit(id));
}
function renderTruckEdit(id) {
  const el = screenEls["truck-edit"];
  const isNew = id === 0;
  const t = isNew ? { plateNumber:"", vehicleType:"", loadCapacityKg:0, bodyType:"OTHER", makerModel:"", notes:"" }
                  : findTruck(id);
  el.innerHTML = `
    <div class="top-bar">
      <button class="icon-btn" data-back><span class="material-symbols-outlined">arrow_back</span></button>
      <h2>${isNew ? "車両を追加" : "車両を編集"}</h2>
      ${isNew ? "" : `<button class="icon-btn" data-delete><span class="material-symbols-outlined">delete</span></button>`}
    </div>
    <div class="scroll-area"><div class="edit-form">
      <div class="field"><label>プレートナンバー</label><div class="value">${t.plateNumber || "&nbsp;"}</div></div>
      <div class="field"><label>車種 (例: 4t, 10t)</label><div class="value">${t.vehicleType || "&nbsp;"}</div></div>
      <div class="field"><label>最大積載量 (kg)</label><div class="value">${t.loadCapacityKg || "&nbsp;"}</div></div>
      <div class="field readonly"><label>車両様式</label>
        <div class="value">${BodyType[t.bodyType]}</div>
        <span class="trail material-symbols-outlined">expand_more</span>
      </div>
      <div class="field"><label>メーカー・車名</label><div class="value">${t.makerModel || "&nbsp;"}</div></div>
      <div class="field multiline"><label>備考</label><div class="value">${t.notes || "&nbsp;"}</div></div>
      <button class="btn-primary">${isNew ? "登録" : "更新"}</button>
    </div></div>
  `;
  el.querySelector('[data-back]').addEventListener('click', popOverlay);
}

/* ---------- Drivers ---------- */
function renderDrivers() {
  const el = screenEls.drivers;
  const cards = drivers.map(d => `
    <div class="card" data-driver="${d.id}">
      <div class="master-title">${d.name}</div>
      <div class="master-meta">${d.licenseClass||"—"}  ${d.phone||""}</div>
    </div>
  `).join("");
  el.innerHTML = `
    <div class="top-bar"><h2>ドライバー一覧</h2></div>
    <div class="scroll-area"><div class="list">${cards}</div></div>
    <button class="fab" data-fab="add-driver"><span class="material-symbols-outlined">add</span></button>
  `;
  el.querySelectorAll('[data-driver]').forEach(c => c.addEventListener('click', () => {
    openDriverEdit(parseInt(c.dataset.driver,10));
  }));
  el.querySelector('[data-fab=add-driver]').addEventListener('click', () => openDriverEdit(0));
}
function openDriverEdit(id) { pushOverlay("driver-edit", () => renderDriverEdit(id)); }
function renderDriverEdit(id) {
  const el = screenEls["driver-edit"];
  const isNew = id === 0;
  const d = isNew ? { name:"", licenseClass:"", phone:"", notes:"" } : findDriver(id);
  el.innerHTML = `
    <div class="top-bar">
      <button class="icon-btn" data-back><span class="material-symbols-outlined">arrow_back</span></button>
      <h2>${isNew ? "ドライバーを追加" : "ドライバーを編集"}</h2>
      ${isNew ? "" : `<button class="icon-btn" data-delete><span class="material-symbols-outlined">delete</span></button>`}
    </div>
    <div class="scroll-area"><div class="edit-form">
      <div class="field"><label>氏名</label><div class="value">${d.name||"&nbsp;"}</div></div>
      <div class="field"><label>免許区分 (例: 大型, 中型)</label><div class="value">${d.licenseClass||"&nbsp;"}</div></div>
      <div class="field"><label>電話</label><div class="value">${d.phone||"&nbsp;"}</div></div>
      <div class="field multiline"><label>備考</label><div class="value">${d.notes||"&nbsp;"}</div></div>
      <button class="btn-primary">${isNew ? "登録" : "更新"}</button>
    </div></div>
  `;
  el.querySelector('[data-back]').addEventListener('click', popOverlay);
}

/* ---------- Clients ---------- */
function renderClients() {
  const el = screenEls.clients;
  const cards = clients.map(c => `
    <div class="card" data-client="${c.id}">
      <div class="row" style="align-items:flex-start;">
        <div style="flex:1;">
          <div class="master-title">${c.name}</div>
          ${c.address ? `<div class="master-meta">${c.address}</div>` : ""}
          ${(c.contactPerson||c.phone) ? `<div class="master-meta">${c.contactPerson||""}  ${c.phone||""}</div>` : ""}
        </div>
        <span class="chip ${c.kind==='GENERATOR'?'gen':'dis'}">${ClientKind[c.kind]}</span>
      </div>
    </div>
  `).join("");
  el.innerHTML = `
    <div class="top-bar"><h2>取引先一覧</h2></div>
    <div class="scroll-area"><div class="list">${cards}</div></div>
    <button class="fab" data-fab="add-client"><span class="material-symbols-outlined">add</span></button>
  `;
  el.querySelectorAll('[data-client]').forEach(card => card.addEventListener('click', () => {
    openClientEdit(parseInt(card.dataset.client,10));
  }));
  el.querySelector('[data-fab=add-client]').addEventListener('click', () => openClientEdit(0));
}
function openClientEdit(id) { pushOverlay("client-edit", () => renderClientEdit(id)); }
function renderClientEdit(id) {
  const el = screenEls["client-edit"];
  const isNew = id === 0;
  const c = isNew ? { name:"", kind:"GENERATOR", address:"", contactPerson:"", phone:"", notes:"" } : findClient(id);
  el.innerHTML = `
    <div class="top-bar">
      <button class="icon-btn" data-back><span class="material-symbols-outlined">arrow_back</span></button>
      <h2>${isNew ? "取引先を追加" : "取引先を編集"}</h2>
      ${isNew ? "" : `<button class="icon-btn" data-delete><span class="material-symbols-outlined">delete</span></button>`}
    </div>
    <div class="scroll-area"><div class="edit-form">
      <div class="field"><label>取引先名</label><div class="value">${c.name||"&nbsp;"}</div></div>
      <div class="field readonly"><label>区分</label>
        <div class="value">${ClientKind[c.kind]}</div>
        <span class="trail material-symbols-outlined">expand_more</span>
      </div>
      <div class="field"><label>住所</label><div class="value">${c.address||"&nbsp;"}</div></div>
      <div class="field"><label>担当者</label><div class="value">${c.contactPerson||"&nbsp;"}</div></div>
      <div class="field"><label>電話</label><div class="value">${c.phone||"&nbsp;"}</div></div>
      <div class="field multiline"><label>備考</label><div class="value">${c.notes||"&nbsp;"}</div></div>
      <button class="btn-primary">${isNew ? "登録" : "更新"}</button>
    </div></div>
  `;
  el.querySelector('[data-back]').addEventListener('click', popOverlay);
}

/* ---------- Wire up bottom nav ---------- */
document.querySelectorAll('.nav-item').forEach(b => b.addEventListener('click', () => setTab(b.dataset.nav)));

/* ---------- Initial render ---------- */
renderTab();
