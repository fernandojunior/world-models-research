from datetime import date

MACROS = [
    ("Macroação 1 – Planejamento e Fundamentação Conceitual", date(2026,10,1), date(2026,11,30), "Documento de planejamento + baseline conceitual", [
        ("1.1 Escopo conceitual e critérios", date(2026,10,1), date(2026,11,15), "form"),
        ("1.2 Levantamento de artigos e repositório", date(2026,10,15), date(2026,11,30), "form"),
        ("1.3 Guias de fundamentos e glossário", date(2026,10,15), date(2026,11,30), "novo"),
        ("1.4 Mapeamento open source e infraestrutura", date(2026,11,3), date(2026,11,30), "novo"),
        ("1.5 Levantamento inicial de perguntas de pesquisa", date(2026,11,17), date(2026,11,30), "novo"),
    ]),
    ("Macroação 2 – Revisão Bibliográfica Sistemática", date(2026,12,1), date(2027,2,28), "Revisão estruturada e documentada do estado da arte", [
        ("2.1 Leitura crítica e síntese", date(2026,12,1), date(2027,2,28), "form"),
        ("2.2 Relatórios técnicos e mapas conceituais", date(2026,12,1), date(2027,2,28), "form"),
        ("2.3 Comparação entre famílias de World Models", date(2026,12,7), date(2027,1,15), "novo"),
        ("2.4 Revisão de real-to-sim e relação com WM", date(2027,1,18), date(2027,2,12), "novo"),
        ("2.5 Levantamento de benchmarks existentes", date(2027,2,15), date(2027,2,26), "novo"),
    ]),
    ("Macroação 3 – Exploração Prática e Experimental", date(2027,3,1), date(2027,5,31), "Demonstrações conceituais reprodutíveis – códigos, vídeos e tutoriais", [
        ("3.1 Seleção e estudo de implementações", date(2027,3,1), date(2027,3,31), "form"),
        ("3.2 Reprodução de experimentos existentes", date(2027,3,1), date(2027,3,31), "form"),
        ("3.3 Pipeline básico de WM baseado em real-to-sim", date(2027,4,1), date(2027,5,31), "novo"),
        ("3.4 Avaliação e documentação preliminar", date(2027,5,1), date(2027,5,31), "novo"),
        ("3.5 Próximos passos / prorrogação (aprofundamento vs viabilidade finanças)", date(2027,5,1), date(2027,5,31), "novo"),
    ]),
    ("Macroação 4 – Monitoramento e Consolidação", date(2026,11,1), date(2027,9,30), "Relatório final e roadmap de pesquisa futura", [
        ("4.1 Monitoramento contínuo", date(2026,11,1), date(2027,9,30), "form"),
        ("4.2 Redação do artigo", date(2027,6,1), date(2027,8,31), "form"),
        ("4.3 Submissão", date(2027,7,1), date(2027,8,31), "form"),
        ("4.4 Revisão do artigo (peer-review)", date(2027,8,1), date(2027,8,31), "form"),
        ("4.5 Relatório técnico final", date(2027,8,1), date(2027,9,30), "novo"),
    ]),
    ("Macroação 5 – Acompanhamento e Prestação de Contas (nova)", date(2026,10,1), date(2027,9,30), "Plano de Trabalho validado, relatórios mensais ao IEL e atas dos encontros", [
        ("5.1 Relatório mensal ao IEL (dia 25, validação do tutor)", date(2026,10,1), date(2027,9,30), "novo"),
        ("5.2 Encontros quadrimestrais", date(2026,11,1), date(2027,9,30), "novo"),
        ("5.3 Elaboração e validação do Plano de Trabalho", date(2026,10,1), date(2026,10,31), "novo"),
        ("5.4 EAD Inova Talentos", date(2026,10,1), date(2026,12,31), "novo"),
        ("5.5 Relatório final do bolsista", date(2027,9,1), date(2027,9,30), "novo"),
    ]),
]

LO, HI = date(2026,10,1), date(2027,10,1)
W, LEFT, RIGHT = 1180, 470, 20
AX = W - LEFT - RIGHT
ROW = 30
MONTHS = ["out","nov","dez","jan","fev","mar","abr","mai","jun","jul","ago","set"]
MILESTONES = [(date(2026,11,30),"Entrega 1"),(date(2027,2,28),"Entrega 2"),(date(2027,5,31),"Entrega 3"),
              (date(2027,6,2),"Prorrogação"),(date(2027,8,31),"Artigo"),(date(2027,9,30),"Entrega 4")]

def x(d): return LEFT + (d - LO).days / (HI - LO).days * AX
def fmt(d): return f"{d.day:02d}/{d.month:02d}"

def chart(title, ms, me, rows, show_ms=False, deliv=None):
    n = len(rows) + 1
    H = 60 + n * ROW + (44 if show_ms else 8) + (22 if deliv else 0)
    s = [f'<svg viewBox="0 0 {W} {H}" width="100%" font-family="system-ui,sans-serif" font-size="13">']
    s.append(f'<text x="10" y="22" font-size="15" font-weight="600">{title}</text>')
    s.append(f'<text x="{W-RIGHT}" y="22" text-anchor="end" font-size="12" fill="#666">{fmt(ms)}/{ms.year%100} → {fmt(me)}/{me.year%100}</text>')
    top = 40
    for i in range(12):
        m0 = date(2026 + (10 + i - 1)//12, (10 + i - 1) % 12 + 1, 1)
        m1 = date(2026 + (10 + i)//12, (10 + i) % 12 + 1, 1)
        fill = "#f4f4f6" if i % 2 else "#ffffff"
        s.append(f'<rect x="{x(m0):.1f}" y="{top}" width="{x(m1)-x(m0):.1f}" height="{n*ROW+10}" fill="{fill}"/>')
        s.append(f'<text x="{(x(m0)+x(m1))/2:.1f}" y="{top+14}" text-anchor="middle" fill="#555">{MONTHS[i]}</text>')
    # macro bar
    y = top + 22
    s.append(f'<rect x="{x(ms):.1f}" y="{y+4}" width="{x(me+ (date(1,1,2)-date(1,1,1)))-x(ms):.1f}" height="22" rx="4" fill="#333" opacity="0.85"/>')
    s.append(f'<text x="{LEFT-8}" y="{y+19}" text-anchor="end" font-weight="600">{"Vigência da bolsa" if show_ms else "Macroação (timebox)"}</text>')
    for k,(name, a, b, kind) in enumerate(rows):
        y = top + 22 + (k+1)*ROW
        col = "#5b8def" if kind == "form" else "#e0882a"
        x0, x1 = x(a), x(b + (date(1,1,2)-date(1,1,1)))
        s.append(f'<text x="{LEFT-8}" y="{y+19}" text-anchor="end">{name}</text>')
        s.append(f'<rect x="{x0:.1f}" y="{y+6}" width="{max(x1-x0,3):.1f}" height="18" rx="4" fill="{col}" opacity="0.9"/>')
        lab = f"{fmt(a)}–{fmt(b)}"
        if x1 - x0 >= 96:
            s.append(f'<text x="{(x0+x1)/2:.1f}" y="{y+19}" text-anchor="middle" font-size="11.5" fill="#fff" font-weight="600">{lab}</text>')
        elif x1 + 92 < W - RIGHT:
            s.append(f'<text x="{x1+6:.1f}" y="{y+19}" text-anchor="start" font-size="11.5" fill="#444">{lab}</text>')
        else:
            s.append(f'<text x="{x0-6:.1f}" y="{y+19}" text-anchor="end" font-size="11.5" fill="#444">{lab}</text>')
    # timebox boundary lines
    for d in (ms, me + (date(1,1,2)-date(1,1,1))):
        s.append(f'<line x1="{x(d):.1f}" x2="{x(d):.1f}" y1="{top+18}" y2="{top+22+n*ROW}" stroke="#c33" stroke-dasharray="4 3"/>')
    if deliv:
        yd = top + 22 + n*ROW + 16
        xe = x(me + (date(1,1,2)-date(1,1,1)))
        s.append(f'<path d="M{xe:.1f} {yd-9}l6 6l-6 6l-6 -6z" fill="#c33"/>')
        txt = f"Entregável {fmt(me)} — {deliv}"
        right = xe + 12 + len(txt) * 6.4 < W - RIGHT
        s.append(f'<text x="{xe+12 if right else xe-12:.1f}" y="{yd+1}" text-anchor="{"start" if right else "end"}" font-size="12" fill="#333">{txt}</text>')
    if show_ms:
        yb = top + 22 + n*ROW + 14
        for i,(d, lab) in enumerate(MILESTONES):
            yy = yb + (14 if i % 2 else 0)
            s.append(f'<line x1="{x(d):.1f}" x2="{x(d):.1f}" y1="{top+18}" y2="{yy-10}" stroke="#999" stroke-dasharray="2 3"/>')
            anc = "end" if x(d) + 55 > W - RIGHT else ("start" if x(d) - 55 < LEFT else "middle")
            s.append(f'<text x="{x(d):.1f}" y="{yy}" text-anchor="{anc}" font-size="11" fill="#333">{lab} {fmt(d)}</text>')
    s.append('</svg>')
    return "\n".join(s)

parts = []
for t, ms, me, dv, rows in MACROS:
    parts.append(f'<section>{chart(t, ms, me, rows, deliv=dv)}</section>')

# visão geral: todas as macroações
overview_rows = [(t, ms, me, "form" if i < 4 else "novo") for i,(t,ms,me,_,_) in enumerate(MACROS)]
parts.append(f'<section>{chart("Visão geral – sobreposição entre macroações", LO, date(2027,9,30), overview_rows, show_ms=True)}</section>')

html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Cronograma World Models</title>
<style>body{{margin:0;padding:16px;background:#fff;color:#111;font-family:system-ui,sans-serif}}
section{{margin:0 0 28px;border:1px solid #e3e3e3;border-radius:8px;padding:8px 12px}}
.leg span{{display:inline-block;margin-right:16px;font-size:13px}} .leg i{{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:-2px;margin-right:6px}}</style></head>
<body><h2 style="margin:0 0 6px">Cronograma World Models — out/2026 a set/2027</h2>
<p class="leg"><span><i style="background:#333"></i>timebox da macroação</span><span><i style="background:#5b8def"></i>já no form (tutor)</span><span><i style="background:#e0882a"></i>novo</span><span style="color:#c33">┊ limites do timebox</span></p>
{"".join(parts)}</body></html>'''
open("cronograma_macroacoes.html","w",encoding="utf-8").write(html)
print("ok")
