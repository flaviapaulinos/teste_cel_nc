import streamlit.components.v1 as components

def powerbi_dashboard(url):
    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="margin:0;padding:0;overflow:hidden">
            <iframe 
                src="{url}?rs:embed=true&rs:command=Render&rs:device=desktop" 
                style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden;"
                allowfullscreen>
            </iframe>
        </body>
        </html>
        """,
        height=700
    )
