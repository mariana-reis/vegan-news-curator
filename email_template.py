from datetime import datetime


class EmailTemplate:

    @staticmethod
    def get_date_string():
        meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
                 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
        hoje = datetime.now()
        return f"{hoje.day} DE {meses[hoje.month - 1]} DE {hoje.year}"

    @staticmethod
    def build(content: str) -> str:
        data_atual = EmailTemplate.get_date_string()

        return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vegan News Curator - Newsletter</title>
</head>
<body style="margin:0;padding:0;font-family:'Georgia','Times New Roman',serif;background:#f5f5f5">
    <div style="max-width:1000px;margin:20px auto;background:white;box-shadow:0 0 30px rgba(0,0,0,0.2)">
        <div style="padding:40px 50px 20px;border-bottom:3px solid #000;text-align:center">
            <div style="font-size:13px;letter-spacing:3px;color:#333;margin-bottom:8px;text-transform:uppercase">{data_atual}</div>
            <h1 style="font-size:48px;font-weight:700;margin:15px 0 5px 0;letter-spacing:8px;color:#000;line-height:1">VEGAN NEWS</h1>
            <p style="font-size:14px;letter-spacing:2px;color:#555;margin-top:12px;font-style:italic">Notícias Curadas • Sustentabilidade • Inovação Plant-Based</p>
            <div style="width:100%;height:2px;background:linear-gradient(90deg,transparent,#000,transparent);margin:15px 0 0 0"></div>
        </div>
        
        <div style="display:flex;background:#f9f9f9;border-top:1px solid #ddd;border-bottom:2px solid #000">
            <div style="flex:1;padding:12px 20px;border-right:1px solid #ddd;font-size:12px;line-height:1.5;color:#333">
                <div style="font-weight:700;text-transform:uppercase;font-size:11px;color:#000;margin-bottom:3px">📰 Edições</div>
                Saúde • Mercado • Sustentabilidade • Tecnologia • Receitas
            </div>
            <div style="flex:1;padding:12px 20px;border-right:1px solid #ddd;font-size:12px;line-height:1.5;color:#333">
                <div style="font-weight:700;text-transform:uppercase;font-size:11px;color:#000;margin-bottom:3px">🌱 Foco</div>
                Jornalismo Editorial Especializado
            </div>
            <div style="flex:1;padding:12px 20px;font-size:12px;line-height:1.5;color:#333">
                <div style="font-weight:700;text-transform:uppercase;font-size:11px;color:#000;margin-bottom:3px">♻️ Missão</div>
                Informação Verificada e Confiável
            </div>
        </div>
        
        <div style="padding:40px 50px">
            {content}
        </div>
        
        <div style="background:#1a1a1a;color:#e0e0e0;padding:40px 50px;border-top:4px solid #1a472a">
            <div style="font-size:18px;font-weight:700;color:#d4af37;letter-spacing:2px;text-transform:uppercase;margin-bottom:15px">Editorial Final</div>
            <div style="width:50px;height:2px;background:#d4af37;margin:15px 0"></div>
            <p style="font-size:14px;line-height:1.9;color:#e0e0e0;margin-bottom:20px;font-style:italic;max-width:700px">
                A transição para alimentos plant-based não é apenas uma tendência, mas um movimento fundamental que redefine nossa relação com o planeta, a saúde e a inovação. Cada notícia que compartilhamos representa esperança em um futuro mais sustentável.
            </p>
            <div style="font-size:11px;color:#999;margin-top:20px;border-top:1px solid #333;padding-top:15px;letter-spacing:0.5px">
                ✍️ Curado por <strong>Mariana Silva</strong><br>
                © 2024-2025 Vegan News Curator • Curação Editorial Profissional<br>
                Desenvolvido com Azure AI Foundry | Todos os direitos reservados
            </div>
        </div>
    </div>

    <style>
        @media (max-width:768px){{
            div[style*="grid-template-columns"]{{grid-template-columns:1fr !important}}
            h1{{font-size:36px}}
        }}
    </style>
</body>
</html>"""