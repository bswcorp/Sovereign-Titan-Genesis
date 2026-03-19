#include <Arduino.h>
#include "h2k_internal.h"

// Definisi Pin sesuai Skema
#define PIN_ADC 4
#define PIN_LO_PLUS 5
#define PIN_LO_MINUS 18

unsigned long last_beat = 0;
int threshold = 3200; // Ambang batas sinyal ECG, sesuaikan jika perlu

void setup() {
    Serial.begin(115200);
    pinMode(PIN_LO_PLUS, INPUT);
    pinMode(PIN_LO_MINUS, INPUT);
    
    // Set resolusi ADC S3 ke 12-bit (0-4095)
    analogReadResolution(12);
    
    Serial.println(">>> SOVEREIGN TITAN GENESIS STARTING...");
    Serial.println(">>> MODE: H2K BIOMETRIC VALIDATOR");
}

void loop() {
    // Cek apakah elektroda terlepas
    if ((digitalRead(PIN_LO_PLUS) == 1) || (digitalRead(PIN_LO_MINUS) == 1)) {
        // Merciful Intervention: Jangan kirim data jika tidak valid
        static long last_alert = 0;
        if (millis() - last_alert > 2000) {
            Serial.println("[!] SENSOR_DISCONNECTED: Harap tempel elektroda.");
            last_alert = millis();
        }
    } else {
        int ecg_val = analogRead(PIN_ADC);
        
        // Deteksi Puncak Jantung (R-Wave)
        if (ecg_val > threshold) {
            unsigned long now = millis();
            int ibi = now - last_beat;

            // Filter Waktu: Jantung manusia normal tidak mungkin berdetak < 400ms (150 BPM)
            if (ibi > 400 && ibi < 1500) {
                // Konversi Kinetik ke Aksara Signature
                String signature = H2K::Sign(ibi);
                
                Serial.print("QS_MINTED_KEY:");
                Serial.println(signature);
                
                last_beat = now;
                delay(100); // Istirahat sejenak untuk menghindari double count
            }
        }
    }
    delay(1); // Frekuensi sampling 1kHz
}
