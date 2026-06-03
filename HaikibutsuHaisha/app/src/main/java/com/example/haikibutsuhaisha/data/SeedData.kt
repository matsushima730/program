package com.example.haikibutsuhaisha.data

import com.example.haikibutsuhaisha.data.entity.Assignment
import com.example.haikibutsuhaisha.data.entity.BodyType
import com.example.haikibutsuhaisha.data.entity.Client
import com.example.haikibutsuhaisha.data.entity.ClientKind
import com.example.haikibutsuhaisha.data.entity.ContainerStatus
import com.example.haikibutsuhaisha.data.entity.Driver
import com.example.haikibutsuhaisha.data.entity.Truck
import java.time.LocalDate

object SeedData {
    suspend fun seedIfEmpty(db: AppDatabase) {
        val truckDao = db.truckDao()
        val driverDao = db.driverDao()
        val clientDao = db.clientDao()
        val assignmentDao = db.assignmentDao()

        // 既に何かあればスキップ
        val anyTruck = truckDao.getById(1)
        if (anyTruck != null) return

        val t1 = truckDao.upsert(
            Truck(plateNumber = "品川 100 あ 12-34", vehicleType = "4t", loadCapacityKg = 4000,
                bodyType = BodyType.DUMP, makerModel = "いすゞ フォワード")
        )
        val t2 = truckDao.upsert(
            Truck(plateNumber = "品川 100 い 56-78", vehicleType = "10t", loadCapacityKg = 10000,
                bodyType = BodyType.CONTAINER_ARM_ROLL, makerModel = "日野 プロフィア")
        )
        val t3 = truckDao.upsert(
            Truck(plateNumber = "品川 800 う 90-12", vehicleType = "2t", loadCapacityKg = 2000,
                bodyType = BodyType.FLATBED, makerModel = "三菱ふそう キャンター")
        )

        val d1 = driverDao.upsert(Driver(name = "佐藤 健太", licenseClass = "大型", phone = "090-1111-2222"))
        val d2 = driverDao.upsert(Driver(name = "鈴木 大輔", licenseClass = "中型", phone = "090-3333-4444"))
        val d3 = driverDao.upsert(Driver(name = "田中 翔",   licenseClass = "準中型", phone = "090-5555-6666"))

        val gen1 = clientDao.upsert(
            Client(name = "ABC建設(株) 港区現場", kind = ClientKind.GENERATOR,
                address = "東京都港区芝公園4-2-8", contactPerson = "山田", phone = "03-1234-5678")
        )
        val gen2 = clientDao.upsert(
            Client(name = "XYZ工務店 練馬倉庫", kind = ClientKind.GENERATOR,
                address = "東京都練馬区豊玉北2-1-1", contactPerson = "高橋", phone = "03-2345-6789")
        )
        val dis1 = clientDao.upsert(
            Client(name = "東京エコセンター", kind = ClientKind.DISPOSAL,
                address = "東京都江東区青海3-1-1", contactPerson = "受付", phone = "03-9999-0001")
        )
        val dis2 = clientDao.upsert(
            Client(name = "千葉中間処理場", kind = ClientKind.DISPOSAL,
                address = "千葉県市川市原木2-3", contactPerson = "受付", phone = "047-000-1234")
        )

        val today = LocalDate.now()
        listOf(
            Assignment(date = today.toString(), truckId = t1, driverId = d1,
                generatorClientId = gen1, disposalClientId = dis1,
                wasteType = "コンクリートがら", departureTime = "08:00", returnTime = "11:30",
                containerStatus = ContainerStatus.EMPTY, notes = "ゲート前で受付"),
            Assignment(date = today.toString(), truckId = t2, driverId = d2,
                generatorClientId = gen2, disposalClientId = dis2,
                wasteType = "木くず", departureTime = "09:00", returnTime = "13:00",
                containerStatus = ContainerStatus.LOADING),
            Assignment(date = today.plusDays(1).toString(), truckId = t3, driverId = d3,
                generatorClientId = gen1, disposalClientId = dis1,
                wasteType = "汚泥", departureTime = "07:30", returnTime = "10:30",
                containerStatus = ContainerStatus.EMPTY)
        ).forEach { assignmentDao.upsert(it) }
    }
}
