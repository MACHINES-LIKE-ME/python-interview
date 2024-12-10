from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr, HttpUrl

class Name(BaseModel):
    title: str
    first: str
    last: str

class Street(BaseModel):
    number: int
    name: str

class Coordinates(BaseModel):
    latitude: str
    longitude: str

class Timezone(BaseModel):
    offset: str
    description: str

class Location(BaseModel):
    street: Street
    city: str
    state: str
    country: str
    postcode: Union[str, int]
    coordinates: Coordinates
    timezone: Timezone

class Login(BaseModel):
    uuid: str
    username: str
    password: str
    salt: str
    md5: str
    sha1: str
    sha256: str

class DateOfBirth(BaseModel):
    date: str
    age: int

class Registered(BaseModel):
    date: str
    age: int

class Id(BaseModel):
    name: Optional[str]
    value: Optional[str]

class Picture(BaseModel):
    large: HttpUrl
    medium: HttpUrl
    thumbnail: HttpUrl

class User(BaseModel):
    gender: str
    name: Name
    location: Location
    email: EmailStr
    login: Login
    dob: DateOfBirth
    registered: Registered
    phone: str
    cell: str
    id: Id
    picture: Picture
    nat: str

class Info(BaseModel):
    seed: str
    results: int
    page: int
    version: str

class RandomUserResponse(BaseModel):
    results: List[User]
    info: Info
