import uproot

# wget https://www.desy.de/\~tadej/tutorial/Zmumu.root
file = uproot.open("Zmumu.root")
tree = file['physics']

df = tree.arrays(library='pd')
df.describe()
print(df.head())
print(df.info())