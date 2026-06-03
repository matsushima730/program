package com.example.haikibutsuhaisha.data.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

/** 車両様式 (車体タイプ) */
enum class BodyType(val label: String) {
    DUMP("ダンプ"),
    FLATBED("平ボディ"),
    CONTAINER_ARM_ROLL("アームロール"),
    CONTAINER_FIXED("コンテナ車"),
    WING("ウイング車"),
    TANK("タンクローリー"),
    OTHER("その他");

    companion object {
        fun fromName(name: String?): BodyType = entries.firstOrNull { it.name == name } ?: OTHER
    }
}

@Entity(tableName = "trucks")
data class Truck(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    /** プレートナンバー (例: 品川 100 あ 12-34) */
    val plateNumber: String,
    /** 車種 (例: 4t / 10t / 2t) */
    val vehicleType: String,
    /** 最大積載量 (kg) */
    val loadCapacityKg: Int,
    /** 車両様式 */
    val bodyType: BodyType = BodyType.OTHER,
    /** メーカー・車名 (任意) */
    val makerModel: String = "",
    val notes: String = ""
)
