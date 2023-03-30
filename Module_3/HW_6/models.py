import json

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Sale(Base):
    __tablename__ = 'sale'
    id_sale = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime(timezone=True), nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id_stock'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock = relationship('Stock', back_populates='sale')


class Stock(Base):
    __tablename__ = 'stock'
    id_stock = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id_book'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id_shop'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    sale = relationship('Sale', back_populates='stock')
    book = relationship('Book', back_populates='stock')
    shop = relationship('Shop', back_populates='stock')


class Book(Base):
    __tablename__ = 'book'
    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id_publisher'), nullable=False)
    stock = relationship('Stock', back_populates='book')
    publisher = relationship('Publisher', back_populates='book')


class Shop(Base):
    __tablename__ = 'shop'
    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), nullable=False)
    stock = relationship('Stock', back_populates='shop')


class Publisher(Base):
    __tablename__ = 'publisher'
    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), nullable=False)
    book = relationship('Book', back_populates='publisher')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def load_data(my_session):
    with open('fixtures\\tests_data.json', 'r', encoding='utf-8') as initial_data:
        test_data = json.load(initial_data)

    for element in test_data:
        if element['model'] == 'publisher':
            my_record = Publisher(id_publisher=element['pk'], name=element['fields']['name'])
            my_session.add(my_record)
        elif element['model'] == 'book':
            my_record = Book(id_book=element['pk'], title=element['fields']['title'],
                             id_publisher=element['fields']['id_publisher'])
            my_session.add(my_record)
        elif element['model'] == 'shop':
            my_record = Shop(id_shop=element['pk'], name=element['fields']['name'])
            my_session.add(my_record)
        elif element['model'] == 'stock':
            my_record = Stock(id_stock=element['pk'], id_book=element['fields']['id_book'],
                              id_shop=element['fields']['id_shop'], count=element['fields']['count'])
            my_session.add(my_record)
        elif element['model'] == 'sale':
            my_record = Sale(id_sale=element['pk'], price=element['fields']['price'],
                             date_sale=element['fields']['date_sale'], count=element['fields']['count'],
                             id_stock=element['fields']['id_stock'])
            my_session.add(my_record)


def get_by_id(my_session, p_id):
    my_query = my_session.query(Publisher.name, Book.title, Sale.price, Sale.date_sale).filter_by(id_publisher=p_id)
    my_query = my_query.join(Book, Book.id_publisher == Publisher.id_publisher)
    my_query = my_query.join(Stock, Stock.id_book == Book.id_book)
    my_query = my_query.join(Shop, Shop.id_shop == Stock.id_shop)
    my_query = my_query.join(Sale, Sale.id_stock == Stock.id_stock)
    my_records_ = my_query.all()
    return my_records_


def get_by_name(my_session, p_name):
    my_query = my_session.query(Publisher.name, Book.title, Sale.price, Sale.date_sale).filter_by(name=p_name)
    my_query = my_query.join(Book, Book.id_publisher == Publisher.id_publisher)
    my_query = my_query.join(Stock, Stock.id_book == Book.id_book)
    my_query = my_query.join(Shop, Shop.id_shop == Stock.id_shop)
    my_query = my_query.join(Sale, Sale.id_stock == Stock.id_stock)
    my_records_ = my_query.all()
    return my_records_


def output(my_records_):
    for element in my_records_:
        print(f'{element[1]} | {element[0]} | {element[2]} | {element[3].date()}')
