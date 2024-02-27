class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def calcular_salario(self):
        pass  

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso,
                 salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)

class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso,
                 sueldo_basico, anios_en_empresa):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico
        self.anios_en_empresa = anios_en_empresa

    def calcular_salario(self):
        if self.anios_en_empresa < 2:
            return self.sueldo_basico
        elif 2 <= self.anios_en_empresa <= 5:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico * 1.10

empleados = [
    EmpleadoComision(1234, "victor", "Perez", 2018, 0, 5, 50),
    EmpleadoSalarioFijo(2345, "mariela", "Gonzalez", 2015, 2000, 4),
    EmpleadoComision(3456, "victoria", "Rodriguez", 2020, 800, 8, 40),
    EmpleadoSalarioFijo(4567, "juan", "Lopez", 2016, 2110, 6),
    EmpleadoComision(54567, "camila", "romero", 2010, 810, 7, 43),
    EmpleadoSalarioFijo(6789, "jose", "martinez", 2015, 2220, 5),
    EmpleadoComision(7891, "lorena", "sanchez", 2021, 870, 9, 3),
    EmpleadoSalarioFijo(89122, "cristian", "gomez", 2017, 2350, 6),
    EmpleadoComision(91234, "javier", "moreno", 2022, 890, 8, 47),
    EmpleadoSalarioFijo(54321, "romina", "leguizamon", 2023, 2400, 1),

]

def mostrar_salarios(empleados):
    for emp in empleados:
        salario = emp.calcular_salario()
        print(f"{emp.nombre} {emp.apellido}: ${salario:.2f}")

mostrar_salarios(empleados)
def empleado_con_mas_clientes(empleados):
    max_clientes = 0
    empleado_max_clientes = None
    for emp in empleados:
        if isinstance(emp, EmpleadoComision):
            if emp.clientes_captados > max_clientes:
                max_clientes = emp.clientes_captados
                empleado_max_clientes = emp
    return empleado_max_clientes

empleado_max_clientes = empleado_con_mas_clientes(empleados)
if empleado_max_clientes:
    print(f"Empleado con más clientes captados: {empleado_max_clientes.nombre} {empleado_max_clientes.apellido}")
else:
    print("No hay empleados a comisión en la lista.")