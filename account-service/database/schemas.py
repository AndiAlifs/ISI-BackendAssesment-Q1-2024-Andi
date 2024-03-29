# Basemodel adalah class yang digunakan untuk memvalidasi data yang dikirimkan oleh client.
from pydantic import BaseModel

# menerima request terkait accout
class AccountRequest(BaseModel):
    nik: str
    nama: str
    no_hp: str
    pin: str

    class Config:
        from_attributes = True

# menerima request terkait transaksi
class TransaksiRequest(BaseModel):
    no_rekening: str
    nominal: int

    class Config:
        from_attributes = True

class TransferRequest(BaseModel):
    no_rekening_asal: str
    no_rekening_tujuan: str
    nominal: int

    class Config:
        from_attributes = True