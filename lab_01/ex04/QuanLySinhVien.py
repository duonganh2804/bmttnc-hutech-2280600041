form Sinhvien import Sinhvien
class QuanLySinhVien:
    listSinhVien = []
    def gennerateId(self):
        maxID=1
        if( self.soluongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID= maxID+1
        return maxID