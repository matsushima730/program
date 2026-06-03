package com.example.haikibutsuhaisha.data.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

/** 取引先種別 (排出事業者 or 処分場) */
enum class ClientKind(val label: String) {
    GENERATOR("排出事業者"),
    DISPOSAL("処分場/中間処理")
}

@Entity(tableName = "clients")
data class Client(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val name: String,
    val kind: ClientKind = ClientKind.GENERATOR,
    val address: String = "",
    val contactPerson: String = "",
    val phone: String = "",
    val notes: String = ""
)
