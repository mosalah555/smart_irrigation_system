import json
from pathlib import Path
import joblib,pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier,HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_recall_fscore_support,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from research_config import CROPS,FEATURES
SEED=20260814;NUM=FEATURES[:4]+[FEATURES[-1]];CAT=["growth_stage","soil_type"]
def pipe(est):return Pipeline([("preprocess",ColumnTransformer([("num",StandardScaler(),NUM),("cat",OneHotEncoder(handle_unknown="ignore"),CAT)])),("classifier",est)])
def train(crop,root):
 d=pd.read_csv(root/"data"/f"{crop}_synthetic.csv");x=d[FEATURES];y=d.irrigation_required;xtr,xtmp,ytr,ytmp=train_test_split(x,y,test_size=.3,stratify=y,random_state=SEED);xv,xte,yv,yte=train_test_split(xtmp,ytmp,test_size=.5,stratify=ytmp,random_state=SEED)
 options={"logistic_regression":LogisticRegression(max_iter=500,class_weight="balanced"),"random_forest":RandomForestClassifier(n_estimators=160,max_depth=12,min_samples_leaf=4,class_weight="balanced",random_state=SEED,n_jobs=-1),"hist_gradient_boosting":HistGradientBoostingClassifier(max_iter=150,max_leaf_nodes=20,random_state=SEED)};scored=[]
 for name,est in options.items():
  model=pipe(est).fit(xtr,ytr);f1=precision_recall_fscore_support(yv,model.predict(xv),average="binary",zero_division=0)[2];scored.append((f1,name,model))
 _,name,model=max(scored);pred=model.predict(xte);p,r,f1,_=precision_recall_fscore_support(yte,pred,average="binary",zero_division=0);result={"crop":crop,"model_type":name,"synthetic_data":True,"training_samples":len(xtr),"validation_samples":len(xv),"test_samples":len(xte),"features":FEATURES,"feature_order":FEATURES,"target":"irrigation_required","accuracy":accuracy_score(yte,pred),"precision":p,"recall":r,"f1":f1,"confusion_matrix":confusion_matrix(yte,pred).tolist()};(root/"models").mkdir(exist_ok=True);(root/"model_results").mkdir(exist_ok=True);joblib.dump(model,root/"models"/f"{crop}_model.joblib");(root/"models"/f"{crop}_metadata.json").write_text(json.dumps(result,indent=2));(root/"model_results"/f"{crop}_results.json").write_text(json.dumps(result,indent=2));return result
if __name__=="__main__":
 root=Path(__file__).resolve().parents[1]
 for crop in CROPS:print(json.dumps(train(crop,root),indent=2))
