#include <Arduino.h>
#include "esp_adc_cal.h"

// Pin Sensor Biometrik (Contoh: Pulse Sensor di GPIO 4)
#define SIGNAL_PIN 4
#define THRESHOLD 550  // Ambang batas detak

// Variabel Filter & Timing
float filter_alpha = 0.75;
float low_pass_filtered = 0;
unsigned long last_beat_time = 0;
int ibi = 600; // Inter-Beat Interval

// Fungsi Kriptografi Aksara Sederhana (H2K-Internal)
String generate_aksara_hash(int value) {
    char buf[10];
    sprintf(buf, "%04X", value ^ 0x1945); // XOR dengan kunci Nusantara
    return String(buf);
}

void setup() {
    Serial.begin(115200);
    analogReadResolution(12); // 12-bit untuk akurasi tinggi pada S3
    pinMode(SIGNAL_PIN, INPUT);
    Serial.println("H2K Node: Sovereign Titan Genesis Online");
}

void loop() {
    int raw_value = analogRead(SIGNAL_PIN);
    
    // Low Pass Filter untuk akurasi tinggi
    low_pass_filtered = (filter_alpha * low_pass_filtered) + ((1 - filter_alpha) * raw_value);
    
    // Logika Deteksi Peak (Detak Jantung)
    if (low_pass_filtered > THRESHOLD) {
        unsigned long current_time = millis();
        if (current_time - last_beat_time > 300) { // Debounce 300ms
            ibi = current_time - last_beat_time;
            last_beat_time = current_time;

            // Generate State Signature berdasarkan IBI (Kinetik)
            String aksara_sig = generate_aksara_hash(ibi);
            
            // Kirim ke Quorum-State via Mesh
            Serial.printf("BEAT DETECTED | IBI: %d | SIG: %s\n", ibi, aksara_sig.c_str());
            
            // Di sini panggil fungsi ESP-NOW untuk broadcast ke Titan-Engine
        }
    }
    delay(2); // Sampling rate 500Hz
}
