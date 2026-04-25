from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# تفعيل CORS للسماح للواجهة بالاتصال بالخادم
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_handler(request: MessageRequest):
    msg = request.message.lower()
    
    # منطق الوكلاء الذكي (التوجيه)
    if "تحليل" in msg:
        reply = "وكيل تحليل السوق: جاري فحص الرسوم البيانية.. المؤشرات توحي باتجاه صاعد."
    elif "مخاطر" in msg:
        reply = "وكيل المخاطر: تنبيه! نسبة التذبذب عالية، يفضل تأمين المحفظة."
    else:
        reply = f"لقد استلمت رسالتك: '{request.message}'. جاري التنسيق مع وكلاء FlashDeal."
    
    return {"reply": reply}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
