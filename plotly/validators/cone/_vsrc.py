import _plotly_utils.basevalidators


class VsrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(self, plotly_name='vsrc', parent_name='cone', **kwargs):
        super(VsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )