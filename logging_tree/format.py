"""Routines that pretty-print a hierarchy of logging `Node` objects."""
import logging


def describe(node):
    """Generate lines describing the given `node` tuple.

    The `node` should be a tuple returned by `logging_tree.nodes.tree()`.

    """
    return _describe(node, None)

def _describe(node, parent):
    """Generate lines describing the given `node` tuple.

    This is the recursive back-end that powers ``describe()``.  With its
    extra ``parent`` parameter, this routine remembers the nearest
    non-placeholder ancestor so that it can compare it against the
    actual value of the ``.parent`` attribute of each node.

    """
    name, logger, children = node
    if not logger.propagate:
        arrow = '   '
    else:
        arrow = '<--'
    yield '%s"%s"' % (arrow, name)

    if logger.level == logging.NOTSET:
        yield '   Level NOTSET so inherits level ' + logging.getLevelName(
            logger.getEffectiveLevel())
    else:
        yield '   Level ' + logging.getLevelName(logger.level)
    if not logger.propagate:
        yield '   Propagate OFF'
    if logger.disabled:
        yield '   Disabled'
