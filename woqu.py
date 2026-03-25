class student:
    name=None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
stu_1=student()

stu_1.name="lele"
stu_1.ring()