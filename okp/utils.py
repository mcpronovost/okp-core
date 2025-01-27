from django.utils.text import slugify


def get_abbr(string, max=2):
    """
    Get an abbreviation from a string.

    Args:
        string (str): The string to get an abbreviation from.
        max (int): The maximum length of the abbreviation.

    Returns:
        str: The abbreviation.
    """
    parts = string.split()
    if not parts:
        return string

    # Handle single word case
    if len(parts) == 1:
        return parts[0][0].upper()

    # Start with first and last letters
    abbr = [parts[0][0]]
    if len(parts) > 1:
        abbr.append(parts[-1][0])

    # Fill middle letters if we have room
    if len(abbr) < max:
        middle_letters = (word[0] for word in parts[1:-1])
        abbr[1:1] = list(middle_letters)[:max - len(abbr)]

    return "".join(abbr).upper()[:max]


def get_slug(string, instance, model):
    """
    Get a slug from a string.

    Args:
        string (str): The string to get a slug from.
        instance (Model): The instance to check for uniqueness.
        model (Model): The model to check for uniqueness.

    Returns:
        str: The slug.
    """
    base_slug = slugify(string)
    slug = base_slug
    counter = 1

    # Check if slug exists and increment counter until unique
    while model.objects.filter(slug=slug).exclude(id=instance.id).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
