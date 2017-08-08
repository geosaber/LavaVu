# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _LavaVuPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_LavaVuPython')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_LavaVuPython')
    _LavaVuPython = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_LavaVuPython', [dirname(__file__)])
        except ImportError:
            import _LavaVuPython
            return _LavaVuPython
        if fp is not None:
            try:
                _mod = imp.load_module('_LavaVuPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _LavaVuPython = swig_import_helper()
    del swig_import_helper
else:
    import _LavaVuPython
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _LavaVuPython.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_LavaVuPython.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_LavaVuPython.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_LavaVuPython.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_LavaVuPython.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_LavaVuPython.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_LavaVuPython.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_LavaVuPython.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_LavaVuPython.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_LavaVuPython.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_LavaVuPython.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_LavaVuPython.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_LavaVuPython.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_LavaVuPython.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_LavaVuPython.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_LavaVuPython.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_LavaVuPython.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _LavaVuPython.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _LavaVuPython.SHARED_PTR_DISOWN
class Line(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _LavaVuPython.Line_swiginit(self, _LavaVuPython.new_Line(*args))
    __swig_destroy__ = _LavaVuPython.delete_Line
Line.iterator = new_instancemethod(_LavaVuPython.Line_iterator, None, Line)
Line.__nonzero__ = new_instancemethod(_LavaVuPython.Line___nonzero__, None, Line)
Line.__bool__ = new_instancemethod(_LavaVuPython.Line___bool__, None, Line)
Line.__len__ = new_instancemethod(_LavaVuPython.Line___len__, None, Line)
Line.__getslice__ = new_instancemethod(_LavaVuPython.Line___getslice__, None, Line)
Line.__setslice__ = new_instancemethod(_LavaVuPython.Line___setslice__, None, Line)
Line.__delslice__ = new_instancemethod(_LavaVuPython.Line___delslice__, None, Line)
Line.__delitem__ = new_instancemethod(_LavaVuPython.Line___delitem__, None, Line)
Line.__getitem__ = new_instancemethod(_LavaVuPython.Line___getitem__, None, Line)
Line.__setitem__ = new_instancemethod(_LavaVuPython.Line___setitem__, None, Line)
Line.pop = new_instancemethod(_LavaVuPython.Line_pop, None, Line)
Line.append = new_instancemethod(_LavaVuPython.Line_append, None, Line)
Line.empty = new_instancemethod(_LavaVuPython.Line_empty, None, Line)
Line.size = new_instancemethod(_LavaVuPython.Line_size, None, Line)
Line.swap = new_instancemethod(_LavaVuPython.Line_swap, None, Line)
Line.begin = new_instancemethod(_LavaVuPython.Line_begin, None, Line)
Line.end = new_instancemethod(_LavaVuPython.Line_end, None, Line)
Line.rbegin = new_instancemethod(_LavaVuPython.Line_rbegin, None, Line)
Line.rend = new_instancemethod(_LavaVuPython.Line_rend, None, Line)
Line.clear = new_instancemethod(_LavaVuPython.Line_clear, None, Line)
Line.get_allocator = new_instancemethod(_LavaVuPython.Line_get_allocator, None, Line)
Line.pop_back = new_instancemethod(_LavaVuPython.Line_pop_back, None, Line)
Line.erase = new_instancemethod(_LavaVuPython.Line_erase, None, Line)
Line.push_back = new_instancemethod(_LavaVuPython.Line_push_back, None, Line)
Line.front = new_instancemethod(_LavaVuPython.Line_front, None, Line)
Line.back = new_instancemethod(_LavaVuPython.Line_back, None, Line)
Line.assign = new_instancemethod(_LavaVuPython.Line_assign, None, Line)
Line.resize = new_instancemethod(_LavaVuPython.Line_resize, None, Line)
Line.insert = new_instancemethod(_LavaVuPython.Line_insert, None, Line)
Line.reserve = new_instancemethod(_LavaVuPython.Line_reserve, None, Line)
Line.capacity = new_instancemethod(_LavaVuPython.Line_capacity, None, Line)
Line_swigregister = _LavaVuPython.Line_swigregister
Line_swigregister(Line)

class Array(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _LavaVuPython.Array_swiginit(self, _LavaVuPython.new_Array(*args))
    __swig_destroy__ = _LavaVuPython.delete_Array
Array.iterator = new_instancemethod(_LavaVuPython.Array_iterator, None, Array)
Array.__nonzero__ = new_instancemethod(_LavaVuPython.Array___nonzero__, None, Array)
Array.__bool__ = new_instancemethod(_LavaVuPython.Array___bool__, None, Array)
Array.__len__ = new_instancemethod(_LavaVuPython.Array___len__, None, Array)
Array.__getslice__ = new_instancemethod(_LavaVuPython.Array___getslice__, None, Array)
Array.__setslice__ = new_instancemethod(_LavaVuPython.Array___setslice__, None, Array)
Array.__delslice__ = new_instancemethod(_LavaVuPython.Array___delslice__, None, Array)
Array.__delitem__ = new_instancemethod(_LavaVuPython.Array___delitem__, None, Array)
Array.__getitem__ = new_instancemethod(_LavaVuPython.Array___getitem__, None, Array)
Array.__setitem__ = new_instancemethod(_LavaVuPython.Array___setitem__, None, Array)
Array.pop = new_instancemethod(_LavaVuPython.Array_pop, None, Array)
Array.append = new_instancemethod(_LavaVuPython.Array_append, None, Array)
Array.empty = new_instancemethod(_LavaVuPython.Array_empty, None, Array)
Array.size = new_instancemethod(_LavaVuPython.Array_size, None, Array)
Array.swap = new_instancemethod(_LavaVuPython.Array_swap, None, Array)
Array.begin = new_instancemethod(_LavaVuPython.Array_begin, None, Array)
Array.end = new_instancemethod(_LavaVuPython.Array_end, None, Array)
Array.rbegin = new_instancemethod(_LavaVuPython.Array_rbegin, None, Array)
Array.rend = new_instancemethod(_LavaVuPython.Array_rend, None, Array)
Array.clear = new_instancemethod(_LavaVuPython.Array_clear, None, Array)
Array.get_allocator = new_instancemethod(_LavaVuPython.Array_get_allocator, None, Array)
Array.pop_back = new_instancemethod(_LavaVuPython.Array_pop_back, None, Array)
Array.erase = new_instancemethod(_LavaVuPython.Array_erase, None, Array)
Array.push_back = new_instancemethod(_LavaVuPython.Array_push_back, None, Array)
Array.front = new_instancemethod(_LavaVuPython.Array_front, None, Array)
Array.back = new_instancemethod(_LavaVuPython.Array_back, None, Array)
Array.assign = new_instancemethod(_LavaVuPython.Array_assign, None, Array)
Array.resize = new_instancemethod(_LavaVuPython.Array_resize, None, Array)
Array.insert = new_instancemethod(_LavaVuPython.Array_insert, None, Array)
Array.reserve = new_instancemethod(_LavaVuPython.Array_reserve, None, Array)
Array.capacity = new_instancemethod(_LavaVuPython.Array_capacity, None, Array)
Array_swigregister = _LavaVuPython.Array_swigregister
Array_swigregister(Array)

class List(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _LavaVuPython.List_swiginit(self, _LavaVuPython.new_List(*args))
    __swig_destroy__ = _LavaVuPython.delete_List
List.iterator = new_instancemethod(_LavaVuPython.List_iterator, None, List)
List.__nonzero__ = new_instancemethod(_LavaVuPython.List___nonzero__, None, List)
List.__bool__ = new_instancemethod(_LavaVuPython.List___bool__, None, List)
List.__len__ = new_instancemethod(_LavaVuPython.List___len__, None, List)
List.__getslice__ = new_instancemethod(_LavaVuPython.List___getslice__, None, List)
List.__setslice__ = new_instancemethod(_LavaVuPython.List___setslice__, None, List)
List.__delslice__ = new_instancemethod(_LavaVuPython.List___delslice__, None, List)
List.__delitem__ = new_instancemethod(_LavaVuPython.List___delitem__, None, List)
List.__getitem__ = new_instancemethod(_LavaVuPython.List___getitem__, None, List)
List.__setitem__ = new_instancemethod(_LavaVuPython.List___setitem__, None, List)
List.pop = new_instancemethod(_LavaVuPython.List_pop, None, List)
List.append = new_instancemethod(_LavaVuPython.List_append, None, List)
List.empty = new_instancemethod(_LavaVuPython.List_empty, None, List)
List.size = new_instancemethod(_LavaVuPython.List_size, None, List)
List.swap = new_instancemethod(_LavaVuPython.List_swap, None, List)
List.begin = new_instancemethod(_LavaVuPython.List_begin, None, List)
List.end = new_instancemethod(_LavaVuPython.List_end, None, List)
List.rbegin = new_instancemethod(_LavaVuPython.List_rbegin, None, List)
List.rend = new_instancemethod(_LavaVuPython.List_rend, None, List)
List.clear = new_instancemethod(_LavaVuPython.List_clear, None, List)
List.get_allocator = new_instancemethod(_LavaVuPython.List_get_allocator, None, List)
List.pop_back = new_instancemethod(_LavaVuPython.List_pop_back, None, List)
List.erase = new_instancemethod(_LavaVuPython.List_erase, None, List)
List.push_back = new_instancemethod(_LavaVuPython.List_push_back, None, List)
List.front = new_instancemethod(_LavaVuPython.List_front, None, List)
List.back = new_instancemethod(_LavaVuPython.List_back, None, List)
List.assign = new_instancemethod(_LavaVuPython.List_assign, None, List)
List.resize = new_instancemethod(_LavaVuPython.List_resize, None, List)
List.insert = new_instancemethod(_LavaVuPython.List_insert, None, List)
List.reserve = new_instancemethod(_LavaVuPython.List_reserve, None, List)
List.capacity = new_instancemethod(_LavaVuPython.List_capacity, None, List)
List_swigregister = _LavaVuPython.List_swigregister
List_swigregister(List)

lucMinType = _LavaVuPython.lucMinType
lucLabelType = _LavaVuPython.lucLabelType
lucPointType = _LavaVuPython.lucPointType
lucGridType = _LavaVuPython.lucGridType
lucTriangleType = _LavaVuPython.lucTriangleType
lucVectorType = _LavaVuPython.lucVectorType
lucTracerType = _LavaVuPython.lucTracerType
lucLineType = _LavaVuPython.lucLineType
lucShapeType = _LavaVuPython.lucShapeType
lucVolumeType = _LavaVuPython.lucVolumeType
lucMaxType = _LavaVuPython.lucMaxType
lucMinDataType = _LavaVuPython.lucMinDataType
lucVertexData = _LavaVuPython.lucVertexData
lucNormalData = _LavaVuPython.lucNormalData
lucVectorData = _LavaVuPython.lucVectorData
lucColourValueData = _LavaVuPython.lucColourValueData
lucOpacityValueData = _LavaVuPython.lucOpacityValueData
lucRedValueData = _LavaVuPython.lucRedValueData
lucGreenValueData = _LavaVuPython.lucGreenValueData
lucBlueValueData = _LavaVuPython.lucBlueValueData
lucIndexData = _LavaVuPython.lucIndexData
lucXWidthData = _LavaVuPython.lucXWidthData
lucYHeightData = _LavaVuPython.lucYHeightData
lucZLengthData = _LavaVuPython.lucZLengthData
lucRGBAData = _LavaVuPython.lucRGBAData
lucTexCoordData = _LavaVuPython.lucTexCoordData
lucSizeData = _LavaVuPython.lucSizeData
lucLuminanceData = _LavaVuPython.lucLuminanceData
lucRGBData = _LavaVuPython.lucRGBData
lucMaxDataType = _LavaVuPython.lucMaxDataType
class OpenGLViewer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    quitProgram = _swig_property(_LavaVuPython.OpenGLViewer_quitProgram_get, _LavaVuPython.OpenGLViewer_quitProgram_set)

    def __init__(self):
        _LavaVuPython.OpenGLViewer_swiginit(self, _LavaVuPython.new_OpenGLViewer())
    __swig_destroy__ = _LavaVuPython.delete_OpenGLViewer
OpenGLViewer_swigregister = _LavaVuPython.OpenGLViewer_swigregister
OpenGLViewer_swigregister(OpenGLViewer)
cvar = _LavaVuPython.cvar
version = cvar.version

class DrawingObject(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _LavaVuPython.DrawingObject_swiginit(self, _LavaVuPython.new_DrawingObject(*args))
    colourMap = _swig_property(_LavaVuPython.DrawingObject_colourMap_get, _LavaVuPython.DrawingObject_colourMap_set)
    __swig_destroy__ = _LavaVuPython.delete_DrawingObject
DrawingObject_swigregister = _LavaVuPython.DrawingObject_swigregister
DrawingObject_swigregister(DrawingObject)

class ColourMap(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _LavaVuPython.ColourMap_swiginit(self, _LavaVuPython.new_ColourMap(*args))
    getDefaultMapNames = staticmethod(_LavaVuPython.ColourMap_getDefaultMapNames)
    getDefaultMap = staticmethod(_LavaVuPython.ColourMap_getDefaultMap)
    __swig_destroy__ = _LavaVuPython.delete_ColourMap
ColourMap.flip = new_instancemethod(_LavaVuPython.ColourMap_flip, None, ColourMap)
ColourMap.monochrome = new_instancemethod(_LavaVuPython.ColourMap_monochrome, None, ColourMap)
ColourMap_swigregister = _LavaVuPython.ColourMap_swigregister
ColourMap_swigregister(ColourMap)

def ColourMap_getDefaultMapNames():
    return _LavaVuPython.ColourMap_getDefaultMapNames()
ColourMap_getDefaultMapNames = _LavaVuPython.ColourMap_getDefaultMapNames

def ColourMap_getDefaultMap(arg2):
    return _LavaVuPython.ColourMap_getDefaultMap(arg2)
ColourMap_getDefaultMap = _LavaVuPython.ColourMap_getDefaultMap

class GeomData(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    type = _swig_property(_LavaVuPython.GeomData_type_get, _LavaVuPython.GeomData_type_set)

    def __init__(self, draw, type):
        _LavaVuPython.GeomData_swiginit(self, _LavaVuPython.new_GeomData(draw, type))
    __swig_destroy__ = _LavaVuPython.delete_GeomData
GeomData_swigregister = _LavaVuPython.GeomData_swigregister
GeomData_swigregister(GeomData)

class LavaVu(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    viewer = _swig_property(_LavaVuPython.LavaVu_viewer_get, _LavaVuPython.LavaVu_viewer_set)
    amodel = _swig_property(_LavaVuPython.LavaVu_amodel_get, _LavaVuPython.LavaVu_amodel_set)
    aview = _swig_property(_LavaVuPython.LavaVu_aview_get, _LavaVuPython.LavaVu_aview_set)
    aobject = _swig_property(_LavaVuPython.LavaVu_aobject_get, _LavaVuPython.LavaVu_aobject_set)
    binpath = _swig_property(_LavaVuPython.LavaVu_binpath_get, _LavaVuPython.LavaVu_binpath_set)

    def __init__(self, binpath, omegalib=False):
        _LavaVuPython.LavaVu_swiginit(self, _LavaVuPython.new_LavaVu(binpath, omegalib))
    __swig_destroy__ = _LavaVuPython.delete_LavaVu
LavaVu.run = new_instancemethod(_LavaVuPython.LavaVu_run, None, LavaVu)
LavaVu.loadFile = new_instancemethod(_LavaVuPython.LavaVu_loadFile, None, LavaVu)
LavaVu.parseCommands = new_instancemethod(_LavaVuPython.LavaVu_parseCommands, None, LavaVu)
LavaVu.render = new_instancemethod(_LavaVuPython.LavaVu_render, None, LavaVu)
LavaVu.init = new_instancemethod(_LavaVuPython.LavaVu_init, None, LavaVu)
LavaVu.image = new_instancemethod(_LavaVuPython.LavaVu_image, None, LavaVu)
LavaVu.web = new_instancemethod(_LavaVuPython.LavaVu_web, None, LavaVu)
LavaVu.video = new_instancemethod(_LavaVuPython.LavaVu_video, None, LavaVu)
LavaVu.defaultModel = new_instancemethod(_LavaVuPython.LavaVu_defaultModel, None, LavaVu)
LavaVu.colourMap = new_instancemethod(_LavaVuPython.LavaVu_colourMap, None, LavaVu)
LavaVu.getColourMap = new_instancemethod(_LavaVuPython.LavaVu_getColourMap, None, LavaVu)
LavaVu.colourBar = new_instancemethod(_LavaVuPython.LavaVu_colourBar, None, LavaVu)
LavaVu.setState = new_instancemethod(_LavaVuPython.LavaVu_setState, None, LavaVu)
LavaVu.getState = new_instancemethod(_LavaVuPython.LavaVu_getState, None, LavaVu)
LavaVu.getFigures = new_instancemethod(_LavaVuPython.LavaVu_getFigures, None, LavaVu)
LavaVu.getTimeSteps = new_instancemethod(_LavaVuPython.LavaVu_getTimeSteps, None, LavaVu)
LavaVu.addTimeStep = new_instancemethod(_LavaVuPython.LavaVu_addTimeStep, None, LavaVu)
LavaVu.resetViews = new_instancemethod(_LavaVuPython.LavaVu_resetViews, None, LavaVu)
LavaVu.setObject = new_instancemethod(_LavaVuPython.LavaVu_setObject, None, LavaVu)
LavaVu.createObject = new_instancemethod(_LavaVuPython.LavaVu_createObject, None, LavaVu)
LavaVu.getObject = new_instancemethod(_LavaVuPython.LavaVu_getObject, None, LavaVu)
LavaVu.reloadObject = new_instancemethod(_LavaVuPython.LavaVu_reloadObject, None, LavaVu)
LavaVu.loadTriangles = new_instancemethod(_LavaVuPython.LavaVu_loadTriangles, None, LavaVu)
LavaVu.loadColours = new_instancemethod(_LavaVuPython.LavaVu_loadColours, None, LavaVu)
LavaVu.loadLabels = new_instancemethod(_LavaVuPython.LavaVu_loadLabels, None, LavaVu)
LavaVu.clearAll = new_instancemethod(_LavaVuPython.LavaVu_clearAll, None, LavaVu)
LavaVu.clearObject = new_instancemethod(_LavaVuPython.LavaVu_clearObject, None, LavaVu)
LavaVu.clearValues = new_instancemethod(_LavaVuPython.LavaVu_clearValues, None, LavaVu)
LavaVu.clearData = new_instancemethod(_LavaVuPython.LavaVu_clearData, None, LavaVu)
LavaVu.arrayUChar = new_instancemethod(_LavaVuPython.LavaVu_arrayUChar, None, LavaVu)
LavaVu.arrayUInt = new_instancemethod(_LavaVuPython.LavaVu_arrayUInt, None, LavaVu)
LavaVu.arrayFloat = new_instancemethod(_LavaVuPython.LavaVu_arrayFloat, None, LavaVu)
LavaVu.textureUChar = new_instancemethod(_LavaVuPython.LavaVu_textureUChar, None, LavaVu)
LavaVu.textureUInt = new_instancemethod(_LavaVuPython.LavaVu_textureUInt, None, LavaVu)
LavaVu.getGeometryCount = new_instancemethod(_LavaVuPython.LavaVu_getGeometryCount, None, LavaVu)
LavaVu.getGeometry = new_instancemethod(_LavaVuPython.LavaVu_getGeometry, None, LavaVu)
LavaVu.geometryArrayUChar = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayUChar, None, LavaVu)
LavaVu.geometryArrayUInt = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayUInt, None, LavaVu)
LavaVu.geometryArrayFloat = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayFloat, None, LavaVu)
LavaVu.geometryArrayViewFloat = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayViewFloat, None, LavaVu)
LavaVu.geometryArrayViewUInt = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayViewUInt, None, LavaVu)
LavaVu.geometryArrayViewUChar = new_instancemethod(_LavaVuPython.LavaVu_geometryArrayViewUChar, None, LavaVu)
LavaVu.imageBuffer = new_instancemethod(_LavaVuPython.LavaVu_imageBuffer, None, LavaVu)
LavaVu.imageJPEG = new_instancemethod(_LavaVuPython.LavaVu_imageJPEG, None, LavaVu)
LavaVu.imagePNG = new_instancemethod(_LavaVuPython.LavaVu_imagePNG, None, LavaVu)
LavaVu.isoSurface = new_instancemethod(_LavaVuPython.LavaVu_isoSurface, None, LavaVu)
LavaVu.update = new_instancemethod(_LavaVuPython.LavaVu_update, None, LavaVu)
LavaVu.close = new_instancemethod(_LavaVuPython.LavaVu_close, None, LavaVu)
LavaVu.imageArray = new_instancemethod(_LavaVuPython.LavaVu_imageArray, None, LavaVu)
LavaVu.imageDiff = new_instancemethod(_LavaVuPython.LavaVu_imageDiff, None, LavaVu)
LavaVu.queueCommands = new_instancemethod(_LavaVuPython.LavaVu_queueCommands, None, LavaVu)
LavaVu.helpCommand = new_instancemethod(_LavaVuPython.LavaVu_helpCommand, None, LavaVu)
LavaVu.commandList = new_instancemethod(_LavaVuPython.LavaVu_commandList, None, LavaVu)
LavaVu.propertyList = new_instancemethod(_LavaVuPython.LavaVu_propertyList, None, LavaVu)
LavaVu_swigregister = _LavaVuPython.LavaVu_swigregister
LavaVu_swigregister(LavaVu)



