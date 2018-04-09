import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

# 產生授權物件
cred = credentials.Certificate(
    "/Users/Lewis/Desktop/vscode/easy_caculating_test/serviceAccount.json")
# 如果firebase_admin 是 None 就初始化，僅會初始化一次
try:
  firebase_admin.delete_app(firebase_admin.get_app())
except:
  print('尚未初始化過 firebase_admin')
else:
  print('初始化 firebase_admin')
firebase_admin.initialize_app(cred)

# 初始化 資料庫物件
db = firestore.client()

def save_data(collection_name, doc_name, data_set):
  
  # 回傳 firebase 儲存後的訊息
  return db.collection(collection_name).document(doc_name).set(data_set)

#定義 查詢資料 函式
def select(name): 
  # 建立 doc 的參考
  doc_ref = db.collection('Grades').document(name)
  
  try:
    
    # 試著讀取數據
    doc = doc_ref.get()
    
    # 將數據轉換為字典
    data = pd.Series(doc.to_dict())
    
    # 回傳抓到結果
    return data
  
  # 出現例外狀況呢？
  except:
    
    # 列印出提示訊息
    print('你還沒考過試！請重新輸入姓名')
    return None
