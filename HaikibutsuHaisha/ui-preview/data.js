// Sample data — mirrors SeedData.kt
const BodyType = {
  DUMP: "ダンプ", FLATBED: "平ボディ",
  CONTAINER_ARM_ROLL: "アームロール", CONTAINER_FIXED: "コンテナ車",
  WING: "ウイング車", TANK: "タンクローリー", OTHER: "その他"
};
const ClientKind = { GENERATOR: "排出事業者", DISPOSAL: "処分場/中間処理" };
const ContainerStatus = {
  EMPTY: "空", LOADING: "積込中", LOADED: "積載中",
  UNLOADING: "荷下し中", RETURNED: "帰着済"
};

const trucks = [
  { id:1, plateNumber:"品川 100 あ 12-34", vehicleType:"4t",  loadCapacityKg:4000,  bodyType:"DUMP",                makerModel:"いすゞ フォワード", notes:"" },
  { id:2, plateNumber:"品川 100 い 56-78", vehicleType:"10t", loadCapacityKg:10000, bodyType:"CONTAINER_ARM_ROLL", makerModel:"日野 プロフィア",   notes:"" },
  { id:3, plateNumber:"品川 800 う 90-12", vehicleType:"2t",  loadCapacityKg:2000,  bodyType:"FLATBED",            makerModel:"三菱ふそう キャンター", notes:"" }
];
const drivers = [
  { id:1, name:"佐藤 健太", licenseClass:"大型",  phone:"090-1111-2222", notes:"" },
  { id:2, name:"鈴木 大輔", licenseClass:"中型",  phone:"090-3333-4444", notes:"" },
  { id:3, name:"田中 翔",   licenseClass:"準中型", phone:"090-5555-6666", notes:"" }
];
const clients = [
  { id:1, name:"ABC建設(株) 港区現場", kind:"GENERATOR", address:"東京都港区芝公園4-2-8", contactPerson:"山田", phone:"03-1234-5678", notes:"" },
  { id:2, name:"XYZ工務店 練馬倉庫",   kind:"GENERATOR", address:"東京都練馬区豊玉北2-1-1", contactPerson:"高橋", phone:"03-2345-6789", notes:"" },
  { id:3, name:"東京エコセンター",     kind:"DISPOSAL",  address:"東京都江東区青海3-1-1", contactPerson:"受付", phone:"03-9999-0001", notes:"" },
  { id:4, name:"千葉中間処理場",       kind:"DISPOSAL",  address:"千葉県市川市原木2-3",   contactPerson:"受付", phone:"047-000-1234", notes:"" }
];

function todayISO(offset=0) {
  const d = new Date(); d.setDate(d.getDate() + offset);
  const y = d.getFullYear();
  const m = String(d.getMonth()+1).padStart(2,'0');
  const day = String(d.getDate()).padStart(2,'0');
  return `${y}-${m}-${day}`;
}
const assignments = [
  { id:1, date: todayISO(0), truckId:1, driverId:1, generatorClientId:1, disposalClientId:3,
    wasteType:"コンクリートがら", departureTime:"08:00", returnTime:"11:30",
    containerStatus:"EMPTY",   notes:"ゲート前で受付" },
  { id:2, date: todayISO(0), truckId:2, driverId:2, generatorClientId:2, disposalClientId:4,
    wasteType:"木くず",          departureTime:"09:00", returnTime:"13:00",
    containerStatus:"LOADING", notes:"" },
  { id:3, date: todayISO(0), truckId:3, driverId:3, generatorClientId:1, disposalClientId:3,
    wasteType:"汚泥",            departureTime:"13:30", returnTime:"16:00",
    containerStatus:"LOADED",  notes:"午後便" },
  { id:4, date: todayISO(1), truckId:3, driverId:3, generatorClientId:1, disposalClientId:3,
    wasteType:"汚泥",            departureTime:"07:30", returnTime:"10:30",
    containerStatus:"EMPTY",   notes:"" }
];

function findTruck(id){ return trucks.find(t=>t.id===id); }
function findDriver(id){ return drivers.find(d=>d.id===id); }
function findClient(id){ return clients.find(c=>c.id===id); }
