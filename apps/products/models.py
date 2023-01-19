from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class MeasureUnit(BaseModel):
    """ Model definition for MeasureInit"""
    
    # TODO: define your fields here
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        """ Meta definition for MeasureInit """
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'
        
    def __str__(self):
        """ Unicode representaion of MeasureInit"""
        return self.description
        
        
class CategoryProduct(BaseModel):
    """ Model definition for CategoryProduct"""
    
    #TODO: Define your fields here
    description = models.CharField('Descripcion' ,max_length=50, unique=True, null=False, blank=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        """ Meta definition for CategoryProduct"""
        verbose_name = 'Categoría de producto'
        verbose_name_plural = 'Categorías del producto'
        
    def __str__(self):
        """ Unicode representation of CategoryProduct"""
        return self.description
    
class Indicator(BaseModel):
    """ Model definition for Indicator"""
    
    #TODO: Define your fields here
    discount_value = models.PositiveSmallIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        """ Meta definition for Indicator"""
        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'
        
    def __str__(self):
        """ Unicode representation of Indicator"""
        return f'Oferta de la categoria {self.category_product} : {self.discount_value}%'
    
# Main model
class Product(BaseModel):
    """ Model definition for Product"""
    
    #TODO: Define your fields here
    name = models.CharField('Nombre del producto', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripcion del Producto', blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoria del Producto',null=True)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        """ Meta definition for Product"""
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        """ Unicode representation of Product"""
        return self.name