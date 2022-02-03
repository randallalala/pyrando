import justpy as jp

def app():
   wp = jp.QuasarPage()
   h1 = jp.QDiv(a=wp, text="Analysis of course reviews" , classes="text-h3 text-centre q-pa-md")
   p1 = jp.QDiv(a=wp, text="these graphs presents course review analysis" )

   
   return wp

jp.justpy(app)
