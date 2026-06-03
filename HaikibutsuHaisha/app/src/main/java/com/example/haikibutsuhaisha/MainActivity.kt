package com.example.haikibutsuhaisha

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.compose.rememberNavController
import com.example.haikibutsuhaisha.ui.nav.AppBottomBar
import com.example.haikibutsuhaisha.ui.nav.AppNavHost
import com.example.haikibutsuhaisha.ui.theme.HaikibutsuTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent { App() }
    }
}

@Composable
private fun App() {
    HaikibutsuTheme {
        val nav = rememberNavController()
        Scaffold(
            bottomBar = { AppBottomBar(nav) }
        ) { padding ->
            AppNavHost(nav, modifier = Modifier.padding(padding))
        }
    }
}
