import pandas as pd 
import unidecode
###Leer el archivo
ruta="Evaluacion.txt"
with open(ruta,"r",encoding="utf-8") as f:
    lineas=f.readlines()
limp_1=lineas[0].strip().split("*")
nombre=" ".join(limp_1[:2])
limp_2=limp_1[2].strip().split("|")
producto=limp_2[0].strip().split(":")
producto=producto.pop(1)
limp_3=limp_2[1].strip().split("=")
precio=limp_3[1].strip().split(";")
precio=precio.pop(0)
limp_4=limp_3[2].split(";")
ciudad=limp_4[0]
correo=limp_3[3]
###Division primera linea 
print(lineas[0])
print(nombre)
print(producto)
print(precio)
print(ciudad)
print(correo)
###Bucle de todo el conjunto
nombres=[]
productos=[]
precios=[]
ciudades=[]
correos=[]
for linea in lineas:
    limp_1=linea.strip().split("*")
    if len(limp_1)<3:
        continue
    nombre=" ".join(limp_1[:2])
    limp_2=limp_1[2].strip().split("|")
    if len(limp_2)<2:
        continue
    producto=limp_2[0].strip().split(":")
    producto=producto.pop(1)
    limp_3=limp_2[1].strip().split("=")
    if len(limp_3)<2:
        continue
    precio=limp_3[1].strip().split(";")
    precio=precio.pop(0)
    limp_4=limp_3[2].split(";")
    if len(limp_4)<2:
        continue
    ciudad=limp_4[0]
    correo=limp_3[3]
    nombres.append(nombre)
    productos.append(producto)
    precios.append(precio)
    ciudades.append(ciudad)
    correos.append(correo)




df=pd.DataFrame({
    "Nombre":nombres,
    "Producto":productos,
    "Precios":precios,
    "Ciudad":ciudades,
    "Correo":correos,
}
)
###Convierto los tipos de datos a su valor correspondiente
df["Nombre"]=df["Nombre"].astype(str)
df["Producto"]=df["Producto"].astype(str)
df["Precios"]=df["Precios"].astype(float)
df["Ciudad"]=df["Ciudad"].apply(lambda x: unidecode.unidecode(x.lower())).astype(str)
df["Correo"]=df["Correo"].astype(str)
print(df.head())
prom_bogota=df[df["Ciudad"]=="bogota"]
prom_bogota=prom_bogota["Precios"].sum()/len(df[df["Ciudad"]=="bogota"])
prom_medellin=df[df["Ciudad"]=="medellin"]
prom_medellin=prom_medellin["Precios"].sum()/len(df[df["Ciudad"]=="medellin"])
prom_cali=df[df["Ciudad"]=="cali"]
prom_cali=prom_cali["Precios"].sum()/len(df[df["Ciudad"]=="cali"])
prom_cartagena=df[df["Ciudad"]=="cartagena"]
prom_cartagena=prom_cartagena["Precios"].sum()/len(df[df["Ciudad"]=="cartagena"])
promedios=[]
promedios.append({
    "Bogota":prom_bogota,
    "Medellin":prom_medellin,
    "Cali":prom_cali,
    "Cartagena":prom_cartagena,
})
print(promedios)
df.to_excel("evaluacion",index=False)







        




