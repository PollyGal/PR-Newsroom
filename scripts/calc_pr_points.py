#!/usr/bin/env python3
"""
Детерминированный калькулятор PR Points по формуле Skyeng: PR Points = N x MQI.
Арифметику делает этот скрипт, а не языковая модель — для воспроизводимости.
Коэффициенты соответствуют config/scoring-config.md.
"""
import argparse, json, sys

# Коэффициенты MQI (синхронизированы с config/scoring-config.md)
FORMAT_COEF = {"case": 1.5, "interview": 1.2, "comment": 0.5, "mention": 0.2}
KEYMSG_COEF = {"true": 1.0, "false": 0.3}
BRAND_COEF  = {"clear": 1.0, "blurred": 0.5, "none": 0.3}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--format", required=True, choices=FORMAT_COEF.keys())
    p.add_argument("--keymsg", required=True, choices=["true", "false"])
    p.add_argument("--brand", required=True, choices=BRAND_COEF.keys())
    p.add_argument("--N", required=True, type=float)
    a = p.parse_args()

    fc = FORMAT_COEF[a.format]
    kc = KEYMSG_COEF[a.keymsg]
    bc = BRAND_COEF[a.brand]
    mqi = round(fc * kc * bc, 4)
    pr = round(a.N * mqi, 2)

    print(json.dumps({
        "N": a.N, "formatCoef": fc, "keyMsgCoef": kc, "brandCoef": bc,
        "MQI": mqi, "prPoints": pr
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
