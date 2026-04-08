# ══════════════════════════════════════════
#  CLASE — el molde
# ══════════════════════════════════════════
class ECU:

    # ── Constructor ───────────────────────
    # Se ejecuta solo cuando creás un objeto
    # Recibe los atributos iniciales
    def __init__(self, nombre, direccion, version):

        # ATRIBUTOS — características del objeto
        self.nombre    = nombre       # "ecu-2h5s"
        self.direccion = direccion    # 170
        self.version   = version      # "3.5.5.00000023"
        self.estado    = "pendiente"  # valor por defecto

    # ── Métodos — acciones que puede hacer ─
    def actualizar(self, version_nueva):
        self.version = version_nueva
        self.estado  = "actualizada"
        print(f"{self.nombre} actualizada a v{self.version}")

    def verificar_comunicacion(self):
        if self.direccion > 0:
            print(f"{self.nombre} — comunicación OK")
        else:
            print(f"{self.nombre} — SIN comunicación")

    def diagnostico(self):
        print(f"Nombre: {self.nombre} | Dir: {self.direccion} | v{self.version} | {self.estado}")


# ══════════════════════════════════════════
#  OBJETOS — instancias concretas del molde
#  (como Juan y Colu en el pizarrón)
# ══════════════════════════════════════════
ecu_hub  = ECU("ecu-2h5s", 170, "3.5.5.00000023")  # objeto 1
ecu_ctrl = ECU("ecu-3h",   130, "3.5.5.00000013")  # objeto 2
ecu_24s  = ECU("ecu-24s",  110, "20.1.0.0000000")  # objeto 3

# Cada objeto tiene sus propios atributos — independientes entre sí
# igual que Juan tiene edad=27 y Colu tiene su propia edad

# ══════════════════════════════════════════
#  USANDO LOS MÉTODOS
# ══════════════════════════════════════════
ecu_hub.verificar_comunicacion()   # llama al método de ESE objeto
ecu_ctrl.verificar_comunicacion()

ecu_hub.actualizar("3.6.0.00000001")  # solo modifica ecu_hub

print("\n=== DIAGNÓSTICO FINAL ===")
ecu_hub.diagnostico()   # versión nueva
ecu_ctrl.diagnostico()  # versión sin tocar
ecu_24s.diagnostico()   # versión sin tocar