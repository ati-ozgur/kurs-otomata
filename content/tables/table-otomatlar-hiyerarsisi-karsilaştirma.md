| Özellik / Makine | Finite Automata (FA)(Sonlu Otomat) | Pushdown Automata (PDA)(Yığıtlı Otomat) | Linear Bounded Automata (LBA)(Doğrusal Sınırlı Otomat) | Turing Machines (TM)(Turing Makinesi) |
|---|---|---|---|---|
| Chomsky Seviyesi | Tip-3 | Tip-2 | Tip-1 | Tip-0 |
| Geçici Bellek Türü | Yok (Sadece durum/state tutar) | Stack (Yığıt) | Sınırlı Şerit (Girdi boyutuyla sınırlı) | Sonsuz RAM / Şerit (Sonsuz Rastgele Erişim) |
| Bellek Erişim Yöntemi | Erişim yok   LIFO (Son Giren İlk Çıkar: Push / Pop) | Sınırlı alan içerisinde Oku / Yaz & Sola / Sağa Hareket | Şerit boyunca serbest Oku / Yaz & Sola / Sağa Hareket |  |
| Hesaplama Gücü | En Düşük | Orta | Yüksek | En Yüksek (En genel hesaplama modeli) |
| Tanıdığı Dil Türü | Düzenli Diller (Regular Languages) | Bağlamdan Bağımsız Diller (Context-Free - CFL) | Bağlama Duyarlı Diller (Context-Sensitive) | Doğrulanabilir Diller (Recursively Enumerable) |
| İlişkili Gramer | Düzenli Gramer (Regular Grammar) | Context-Free Grammar (CFG) | Context-Sensitive Grammar | Kısıtsız Gramer (Unrestricted Grammar) |
| Örnek Tanıdığı Dil / Yapı | Metin arama, $a^* b^*$ biçimindeki dizilimler | $a^n b^n$ (Eşit sayıda $a$ ve $b$) | $a^n b^n c^n$ (Üçlü eşitlikler) | Her türlü algoritmik problem |