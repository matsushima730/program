package com.example.haikibutsuhaisha.util

import java.time.LocalDate
import java.time.LocalTime
import java.time.format.DateTimeFormatter
import java.time.format.DateTimeFormatterBuilder
import java.util.Locale

object DateFmt {
    val ISO_DATE: DateTimeFormatter = DateTimeFormatter.ISO_LOCAL_DATE
    val JP_DATE: DateTimeFormatter = DateTimeFormatterBuilder()
        .appendPattern("yyyy年M月d日(E)")
        .toFormatter(Locale.JAPAN)
    val JP_MONTH: DateTimeFormatter = DateTimeFormatter.ofPattern("yyyy年M月", Locale.JAPAN)
    val HOUR: DateTimeFormatter = DateTimeFormatter.ofPattern("HH:mm", Locale.JAPAN)

    fun parseDateOrToday(s: String?): LocalDate =
        runCatching { LocalDate.parse(s, ISO_DATE) }.getOrDefault(LocalDate.now())

    fun parseTimeOrNull(s: String?): LocalTime? =
        s?.takeIf { it.isNotBlank() }?.let { runCatching { LocalTime.parse(it, HOUR) }.getOrNull() }
}
