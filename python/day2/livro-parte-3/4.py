def filecursor(filename):
    """
    >>> g = filecursor('4.txt')
    >>> g.next()
    ('henrique', 'bastos')
    >>> g.next()
    ('cristiane', 'monteiro')
    >>> g.next()
    ('flavio', 'amieiro')
    >>> g.next()
    ('mariana', 'bedran')
    >>> g.next()
    ('bernardo', 'botelho')
    
    >>> g = filecursor('no-file.txt')
    Error
    """
    try:
        with open(filename, 'r') as f:
            for line in f:
                data = tuple(line.strip().split(','))
                yield data
    except:
        print "Error"
    finally:
        f.close()
    return

if __name__ == '__main__':
    import doctest
    doctest.testmod()
