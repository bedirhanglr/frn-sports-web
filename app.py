from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    gunun_maci = {
        "baslik": "Sinner vs. Bonzi",
        "turnuva": "ATP 1000 Madrid",
        "saat": "Şu An", 
        "durum": "Canlı", 
        "embed_link": "https://sportswin.click/play.php?atp-tour/atp-madrid-jannik-sinner-vs-benjamin-bonzi-stream-1"
    }

    # Maçlara "id" ve "embed_link" eklendi
    tum_maclar = [
        {
            "id": 1,
            "baslik": "🇹🇷 Zeynep Sönmez vs. Solana Sierra",
            "turnuva": "WTA 1000 Madrid - Son 32",
            "saat": "25 Nisan 12:00",
            "durum": "Başlamadı",
            "embed_link": "https://taraftarium1049.xyz/"
        }
    ]

    return render_template('index.html', gunun_maci=gunun_maci, tum_maclar=tum_maclar)

# --- YENİ EKLENEN KISIM: Özel İzleme Sayfası Rotası ---
@app.route('/izle/<int:mac_id>')
def izle_sayfasi(mac_id):
    # Tüm maçlar listesi içinden, tıklanan ID'ye sahip maçı buluyoruz
    tum_maclar = [
        {
            "id": 1,
            "baslik": "🇹🇷 Zeynep Sönmez vs. Solana Sierra",
            "embed_link": "https://taraftarium1049.xyz/"
        }
    ]
    
    secilen_mac = next((mac for mac in tum_maclar if mac["id"] == mac_id), None)
    
    if secilen_mac:
        # Eğer maç bulunduysa, o maçı yayin.html sayfasına gönder
        return render_template('yayin.html', mac=secilen_mac)
    else:
        return "Maç bulunamadı!", 404

if __name__ == '__main__':
    app.run(debug=True)
