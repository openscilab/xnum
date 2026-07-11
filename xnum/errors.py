# -*- coding: utf-8 -*-
"""XNum errors."""


class XNumError(Exception):
    """Base exception for all XNum errors."""

class XNumValidationError(XNumError, ValueError):
    """Raised when input validation fails."""
