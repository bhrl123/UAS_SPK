from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Laptop(Base):
    __tablename__ = "laptop"

    id : Mapped[int] = mapped_column(primary_key=True)
    Merk : Mapped[str]
    ram : Mapped[str]
    memori_internal : Mapped[str]
    processor : Mapped[str]
    layar : Mapped[str]
    Harga : Mapped[str]
    baterai_mah : Mapped[str]
    Harga : Mapped[str]

    def __repr__(self) -> str :
        return f"id={self.id}, Merk={self.Merk}, ram={self.ram}, memori_internal={self.memori_internal}, processor={self.processor}, Harga={self.Harga}, baterai_mah={self.baterai_mah}, Harga={self.Harga}"

