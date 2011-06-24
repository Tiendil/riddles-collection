

from django_next.jinja2.decorators import jinjaglobal

@jinjaglobal
def paginator_pages(page_number, total_pages, radius=2):

    pages = []

    if total_pages == 1:
        return pages
    
    if page_number <= radius + 1:
        pages.extend(range(1, page_number + 1))
    else:
        pages.extend([1, None])
        pages.extend(range(page_number-radius, page_number + 1))

    if page_number + radius >= total_pages:
        pages.extend(range(page_number+1, total_pages + 1))
    else:
        pages.extend(range(page_number+1, page_number+radius + 1))        
        pages.extend([None, total_pages])

    return pages
    



    

    
