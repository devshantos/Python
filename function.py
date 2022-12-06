def wp_paragraph(p_text):
    code = f"<!-- wp:heading --><p>{p_text}</p><!-- /wp:heading -->"
    return code

def wp_title(tittle_text):
    code = f"<!-- wp:paragraph --><h3><strong>{tittle_text}</strong></h3><!-- /wp:paragraph -->"
    return code