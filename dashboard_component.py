# dashboard_component.py
import streamlit.components.v1 as components

def powerbi_dashboard(url):
    # Remova os parâmetros problemáticos
    clean_url = url.split('?')[0]  # Mantém apenas a parte base da URL
    
    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        </head>
        <body style="margin:0;padding:0;overflow:hidden">
            <iframe 
                src="{clean_url}?embed=true" 
                style="position:fixed; top:0; left:0; width:100%; height:100%; border:none;"
                frameborder="0"
                allowFullScreen="true">
            </iframe>
        </body>
        </html>
        """,
        height=700
    )