
class employee:
    def assign(self,name,id):
        self.name=name
        self.idno=id
    def show(self):
        print("name:",self.name)
        print("idno:",self.idno)

x=employee()
x.assign()
x.show()

