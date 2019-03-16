import panda_file as pf

from sklearn.tree import DecisionTreeRegressor

mel_mod = DecisionTreeRegressor(random_state=1)

fit = mel_mod.fit(pf.x,pf.y)

a = pf.x.head()

# print(fit)

print("Making predictions:")
print(a)
print("The predictions:")
print(mel_mod.predict(a))
