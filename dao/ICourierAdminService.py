#dao/ICourierAdminService.py

from abc import ABC, abstractmethod
from entity.Employee import Employee
from ICourierUserService import ICourierUserService

class ICourierAdminService(ICourierUserService):
    @abstractmethod
    def addCourierStaff(self, name, contactNumber):
        pass
