
# File 6: README.md - Dokumentimi i projektit

readme = '''# Projekt 3: Oshilatori Duffing - Skanimi i Parametrave dhe Seksionet Poincaré

## Përshkrimi

Ky projekt studion kalimin nga lëkundje të rregullta në dinamikë komplekse për oshilatorin Duffing të detyruar dhe të amortizuar.

## Ekuacioni i Duffing-ut

$$\\ddot{x} + \\delta\\dot{x} + \\alpha x + \\beta x^3 = \\gamma\\cos(\\omega t)$$

### Parametrat:
- **δ** - Koeficienti i amortizimit
- **α** - Koeficienti linear i rigiditetit
- **β** - Koeficienti jolinear (kubik)
- **γ** - Amplituda e forcës së jashtme
- **ω** - Frekuenca e forcës së jashtme

## Struktura e Projektit

```
duffing_poincare_project/
├── README.md                          # Ky file
├── src/
│   ├── models/
│   │   └── duffing.py                 # Modeli matematikor
│   ├── visualization/
│   │   └── phase_plots.py             # Vizualizime
│   └── analysis/
│       └── poincare.py                # Seksione Poincaré dhe skanimi
├── scripts/
│   ├── run_single.py                  # Simulim i vetëm
│   └── scan_forcing.py                # Skanimi i parametrave
└── results/
    └── figures/                       # Figurat e gjeneruara
```

## Instalimi

```bash
# Kërkesat
pip install numpy scipy matplotlib

# Ose përdorni requirements.txt
```

## Përdorimi

### Simulim i vetëm:
```bash
duffing_poincare_project
python scripts/run_single.py
```

Ky script simulon sistemin me parametrat e paracaktuar dhe gjeneron:
- Seritë kohore të pozicionit dhe shpejtësisë
- Portretin fazor (plot dhe regjimi stacionar)
- Grafikun e energjisë efektive
- Seksionin Poincaré

### Skanimi i parametrave:
```bash
python scripts/scan_forcing.py
```

Ky script ekzekuton:
1. **Seksionet Poincaré** për 3 vlera të γ
2. **Diagramin e bifurkacionit** për γ
3. **Krahasimin** me oshilatorin harmonik/anharmonik
4. **Analizën e sensitivitetit** ndaj kushteve fillestare
5. **Skanimin** e ω dhe δ

## Rezultatet e Pritshme

### Regjimi Afërsisht Periodik (γ e vogël)
- Seksioni Poincaré: pika të pakta (1-3), tregon periodicitet
- Portreti fazor: trajektori e mbyllur

### Regjimi me Forcë të Madhe (γ e madhe)
- Seksioni Poincaré: shumë pika, strukturë fraktale
- Tregon dinamikë kaotike ose shumë-periodike

### Ndryshimi Cilësor
Kur rritet forca e jashtme γ:
1. Period 1 → Period 2 → Period 4 → ... → Kaos
2. Dëshmohet bifurkacioni me dyfishim të periodës
3. Seksioni Poincaré tregon "strange attractor"

## Metodologjia

### 1. Konvertimi në Sistem të Rendit të Parë
$$\\dot{x} = v$$
$$\\dot{v} = -\\delta v - \\alpha x - \\beta x^3 + \\gamma\\cos(\\omega t)$$

### 2. Integrimi Numerik
Përdoret `scipy.integrate.solve_ivp` me metodën RK45.
- Hapi maksimal: $T_{driving}/20$ për saktësi
- Tolerancat: rtol=1e-6, atol=1e-9

### 3. Seksioni Poincaré
Kampionimi në kohëra $t_n = nT$ ku $T = 2\\pi/\\omega$.
Anashkalohen 50-100 perioda për eleminimin e transientëve.

### 4. Energjia Efektive
$$E_{eff} = \\frac{1}{2}v^2 + \\frac{1}{2}\\alpha x^2 + \\frac{1}{4}\\beta x^4$$

## Referencat

- Duffing, G. (1918). *Erzwungene Schwingungen bei veränderlicher Eigenfrequenz*
- Strogatz, S. H. (2018). *Nonlinear Dynamics and Chaos*
- Ott, E. (2002). *Chaos in Dynamical Systems*

# Moduli i Oshilatorit Duffing dhe Sistemeve Kaotike – Vjorisa

Ky modul trajton sjelljen komplekse jolineare dhe kaotike të Oshilatorit Duffing. Si **Eksperte e Vizualizimit**, përveç analizës matematiko-fizike të kaosit, jam fokusuar në gjenerimin e grafikëve të avancuar si Portretet Fazore dhe Seksionet Poincaré.

### Bashkëpunimi dhe Ndarja e Kontributeve

* **Ndihma për Azemin & Kejsin:** Kam marrë rolin e "Drejtoreshës së Grafikëve" duke u mësuar të dy anëtarëve përdorimin profesional të librarisë Matplotlib. Kam ndihmuar në rregullimin e legjendave, titujve dhe në ndërtimin e skripteve që i ruajnë fotot automatikisht në direktorinë `/results/figures/`.
* **Ndihma për Analizën:** Kam ndihmuar grupin në interpretimin fizik të hapësirës fazore. Për shembull, kam asistuar Kejsin në analizimin e Portretit të tij Fazor, duke shpjeguar se si spiralizimi i trajektores tregon grafikisht konvergjencën drejt një pike të ekuilibrit fiks.
* **Asistenca e pranuar:** Azemi më ka lehtësuar punën duke më dhënë "skeletin" e kodit të oshilatorit harmonik, mbi të cilin unë thjesht shtova termin jolinear ($x^3$). Kejsi më ka ndihmuar me ekspertizën e tij mbi fërkimin për të rregulluar vlerën e saktë të parametrit $\delta$ (damping), në mënyrë që Seksioni im Poincaré të mos ishte kaotik në pafundësi por të shfaqte strukturat fraktale.

## Autori

Vjorisa Cani - Fizikë dhe Shkenca Kompjuterike
