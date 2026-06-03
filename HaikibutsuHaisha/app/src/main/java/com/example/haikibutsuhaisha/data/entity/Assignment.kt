package com.example.haikibutsuhaisha.data.entity

import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey

/** コンテナ/積載状態 */
enum class ContainerStatus(val label: String) {
    EMPTY("空"),
    LOADING("積込中"),
    LOADED("積載中"),
    UNLOADING("荷下し中"),
    RETURNED("帰着済");

    companion object {
        fun fromName(name: String?): ContainerStatus = entries.firstOrNull { it.name == name } ?: EMPTY
    }
}

/**
 * 1日 × 1配車。
 * date は yyyy-MM-dd 文字列で保持 (Room TypeConverter 不要)。
 * departureTime / returnTime は HH:mm 文字列。
 */
@Entity(
    tableName = "assignments",
    foreignKeys = [
        ForeignKey(
            entity = Truck::class,
            parentColumns = ["id"],
            childColumns = ["truckId"],
            onDelete = ForeignKey.SET_NULL
        ),
        ForeignKey(
            entity = Driver::class,
            parentColumns = ["id"],
            childColumns = ["driverId"],
            onDelete = ForeignKey.SET_NULL
        ),
        ForeignKey(
            entity = Client::class,
            parentColumns = ["id"],
            childColumns = ["generatorClientId"],
            onDelete = ForeignKey.SET_NULL
        ),
        ForeignKey(
            entity = Client::class,
            parentColumns = ["id"],
            childColumns = ["disposalClientId"],
            onDelete = ForeignKey.SET_NULL
        )
    ],
    indices = [
        Index("date"),
        Index("truckId"),
        Index("driverId"),
        Index("generatorClientId"),
        Index("disposalClientId")
    ]
)
data class Assignment(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val date: String,
    val truckId: Long?,
    val driverId: Long?,
    /** 排出元 (取引先) */
    val generatorClientId: Long?,
    /** 行き先 (処分場/中間処理) */
    val disposalClientId: Long?,
    /** 廃棄物種類 (例: 木くず・コンクリートがら・汚泥) */
    val wasteType: String = "",
    /** 発車予定時間 HH:mm */
    val departureTime: String = "",
    /** 帰着予定時間 HH:mm */
    val returnTime: String = "",
    val containerStatus: ContainerStatus = ContainerStatus.EMPTY,
    val notes: String = ""
)
