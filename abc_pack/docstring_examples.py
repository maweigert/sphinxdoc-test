"""
Huhu
"""


def sphynx_style(x, y=None, fname=""):
    """

    :param x: the first value
    :type x: str
    :param y: the second value
    :type y: float, int, ndarray
    :param fname: the name to write to
    :type fname: str
    :return: 1 on sucess
    """

    pass


def rst_style(x, y=None, fname=""):
    """
    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File
       instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor"""
    pass


def google_style(x, y=None, fname=""):
    """

    Args:
        x (int):
            the first value
        y (float):
            nothing
        fname (str):
            obvious

    Returns:
        everything you never cared about
    """
    pass

    # def (x,y = None, fname = ""):


def numpy_style():
    """

    Return a new array of given shape and type, filled with zeros.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.

    Returns
    -------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.

    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    ones_like : Return an array of ones with shape and type of input.
    empty_like : Return an empty array with shape and type of input.
    ones : Return a new array setting values to one.
    empty : Return a new uninitialized array.

    Examples
    --------
    >>> np.zeros(5)
    array([ 0.,  0.,  0.,  0.,  0.])

    >>> np.zeros((5,), dtype=np.int)
    array([0, 0, 0, 0, 0])

    >>> np.zeros((2, 1))
    array([[ 0.],
           [ 0.]])

    >>> s = (2,2)
    >>> np.zeros(s)
    array([[ 0.,  0.],
           [ 0.,  0.]])

    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)],
          dtype=[('x', '<i4'), ('y', '<i4')])
    """
    pass



def citing_me():
    """

    please cite [1]_

    and we do have footnotes [#f1]_ as well!

    .. math::
        e^{-\\alpha x} = \int_0^1 dk f(k)

    .. rubric:: Footnotes

    .. [#f1] Text fo the footnote

    References
    ----------
    .. [1] Hugo Beierthal (2013) *fastsomething: We wish you a merry christmas*

    """