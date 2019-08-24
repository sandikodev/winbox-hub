import snapcraft

class MyPlugin(snapcraft.BasePlugin):
    @classmethod
    def schema(cls):
        schema = super().schema()

        schema['properties']['my-property'] = {
            'type': 'string'
        }
        schema['required'].append('my-property')

        return schema
    def pull(self):
        super().pull()
        print('we have pulled - by {}'.format(self.options.my_property))

    def build(self):
        super().build()
        print('we done')
