package com.example.haikibutsuhaisha.data.entity

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "drivers")
data class Driver(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val name: String,
    /** 免許区分 (例: 大型 / 中型 / 準中型 / 普通) */
    val licenseClass: String = "",
    val phone: String = "",
    val notes: String = ""
)
